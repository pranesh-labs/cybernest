import asyncio
import datetime
import sys
import httpx
import structlog
from shared_python import setup_logging
from shared_python.models import AgentHeartbeat, ScanResultPayload, HostInfo
from agent.fingerprinting.config.settings import agent_settings
from agent.plugins import PluginManager

# Initialize logging
setup_logging(environment=agent_settings.ENVIRONMENT, log_level_str=agent_settings.LOG_LEVEL)
logger = structlog.get_logger()

async def send_heartbeat(client: httpx.AsyncClient) -> None:
    """
    Constructs and transmits heartbeat telemetry to the API backend.
    """
    heartbeat = AgentHeartbeat(
        agent_id=agent_settings.AGENT_ID,
        timestamp=datetime.datetime.utcnow(),
        status="online",
        version="1.0.0",
        system_info={
            "platform": sys.platform,
            "python_version": sys.version,
        }
    )
    url = f"{agent_settings.API_URL}/agent/heartbeat"
    headers = {"X-Agent-Token": agent_settings.AGENT_AUTH_TOKEN}
    
    try:
        response = await client.post(url, json=heartbeat.model_dump(mode='json'), headers=headers)
        if response.status_code == 204:
            await logger.adebug("Heartbeat reported successfully")
        else:
            await logger.awarn("Heartbeat failed", status_code=response.status_code)
    except Exception as e:
        await logger.aerror("Could not send heartbeat to server", error=str(e))

async def run_scan_cycle(client: httpx.AsyncClient, plugin_manager: PluginManager) -> None:
    """
    Runs active plugins and uploads compiled scan results.
    """
    await logger.ainfo("Starting scan cycle...")
    started_at = datetime.datetime.utcnow()

    # Execute all plugins
    target_subnet = "192.168.1.0/24" # Mock local subnet
    plugin_data = await plugin_manager.execute_all(target_subnet)
    
    finished_at = datetime.datetime.utcnow()

    # Assemble scan result payload
    # In a full execution, parse plugin outputs into HostInfo models. Here we report mock data matching types.
    mock_hosts = [
        HostInfo(
            ip="192.168.1.50",
            mac="00:11:22:33:44:55",
            hostname="scanned-device-1",
            os_name="Linux",
            os_version="5.10",
            open_ports=[22, 80, 443]
        )
    ]
    
    payload = ScanResultPayload(
        agent_id=agent_settings.AGENT_ID,
        scan_id=f"scan-{int(started_at.timestamp())}",
        started_at=started_at,
        finished_at=finished_at,
        hosts=mock_hosts,
        vulnerabilities=[]
    )

    url = f"{agent_settings.API_URL}/agent/scan-results"
    headers = {"X-Agent-Token": agent_settings.AGENT_AUTH_TOKEN}
    
    try:
        response = await client.post(url, json=payload.model_dump(mode='json'), headers=headers)
        if response.status_code == 200:
            await logger.ainfo("Scan results uploaded successfully", hosts_reported=len(mock_hosts))
        else:
            await logger.awarn("Scan upload failed", status_code=response.status_code)
    except Exception as e:
        await logger.aerror("Could not upload scan results to server", error=str(e))

async def main() -> None:
    await logger.ainfo(
        "Starting CyberNest Fingerprinting Agent daemon...",
        agent_id=agent_settings.AGENT_ID,
        api_url=agent_settings.API_URL
    )

    # Initialize plugin manager and load scan plugins
    plugin_manager = PluginManager()
    await plugin_manager.load_plugins()

    async with httpx.AsyncClient() as client:
        # Initial heartbeat
        await send_heartbeat(client)

        # Run daemon loop
        loop_counter = 0
        while True:
            await asyncio.sleep(1)
            loop_counter += 1

            if loop_counter % agent_settings.HEARTBEAT_INTERVAL_SECONDS == 0:
                await send_heartbeat(client)

            if loop_counter % agent_settings.SCAN_INTERVAL_SECONDS == 0:
                await run_scan_cycle(client, plugin_manager)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Agent daemon stopped by user")
