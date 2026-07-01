from fastapi import APIRouter, Depends, HTTPException, Security, status
from fastapi.security import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession
from shared_python.models import AgentHeartbeat, ScanResultPayload
from app.core.config import settings
from app.database.session import get_db
from app.services.host import host_service

router = APIRouter()

# API Key header check for agents
api_key_header = APIKeyHeader(name="X-Agent-Token", auto_error=False)

def authenticate_agent(token: str = Depends(api_key_header)) -> str:
    if not token or token != settings.AGENT_AUTH_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Unauthorized agent token",
        )
    return token

@router.post("/heartbeat", status_code=status.HTTP_204_NO_CONTENT)
async def report_heartbeat(
    heartbeat: AgentHeartbeat,
    _token: str = Depends(authenticate_agent),
) -> None:
    """
    Heartbeat endpoint for active scan agents to report state.
    """
    # In practice, log or save heartbeat status to cache
    pass

@router.post("/scan-results", status_code=status.HTTP_200_OK)
async def report_scan_results(
    payload: ScanResultPayload,
    _token: str = Depends(authenticate_agent),
    db: AsyncSession = Depends(get_db)
) -> dict:
    """
    Receive vulnerability scans from agents and upsert to database.
    """
    hosts = await host_service.process_scan_payload(db, payload=payload)
    return {
        "status": "success",
        "processed_hosts": len(hosts),
    }
