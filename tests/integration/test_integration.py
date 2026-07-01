import pytest
from fastapi.testclient import TestClient
from shared_python.models import AgentHeartbeat, ScanResultPayload, HostInfo
from app.main import app
from app.core.config import settings

client = TestClient(app)

def test_integration_flow() -> None:
    """
    Integration test asserting that the Agent can authenticate and push heartbeats
    and scan telemetry successfully through the API endpoints.
    """
    agent_id = "test-agent-integration"
    token = settings.AGENT_AUTH_TOKEN
    headers = {"X-Agent-Token": token}

    # 1. Report Heartbeat
    heartbeat_payload = {
        "agent_id": agent_id,
        "timestamp": "2026-07-02T00:00:00Z",
        "status": "online",
        "version": "1.0.0",
        "system_info": {}
    }
    
    response = client.post(
        "/api/v1/agent/heartbeat", 
        json=heartbeat_payload, 
        headers=headers
    )
    assert response.status_code == 204

    # 2. Upload Scan Result Payload
    scan_payload = {
        "agent_id": agent_id,
        "scan_id": "scan-12345",
        "started_at": "2026-07-02T00:00:00Z",
        "finished_at": "2026-07-02T00:05:00Z",
        "hosts": [
            {
                "ip": "10.0.0.5",
                "mac": "11:22:33:44:55:66",
                "hostname": "target-host",
                "os_name": "Linux",
                "os_version": "5.15",
                "open_ports": [22, 80]
            }
        ],
        "vulnerabilities": []
    }

    response = client.post(
        "/api/v1/agent/scan-results",
        json=scan_payload,
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert response.json()["processed_hosts"] == 1
