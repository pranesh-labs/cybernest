from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class AgentHeartbeat(BaseModel):
    """
    Schema for heartbeat signals sent by fingerprinting agents.
    """
    agent_id: str = Field(..., description="Unique identifier for the agent")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    status: str = Field("online", description="Agent state (e.g., online, scanning, idle)")
    version: str = Field("1.0.0", description="Agent software version")
    system_info: Dict[str, Any] = Field(default_factory=dict, description="OS and resource info")

class HostInfo(BaseModel):
    """
    Sub-schema representing a scanned network host.
    """
    ip: str
    mac: Optional[str] = None
    hostname: Optional[str] = None
    os_name: Optional[str] = None
    os_version: Optional[str] = None
    open_ports: List[int] = Field(default_factory=list)

class VulnerabilityReport(BaseModel):
    """
    Sub-schema for vulnerability scan detections.
    """
    cve_id: str
    severity: str
    description: str
    target_host: str
    port: Optional[int] = None

class ScanResultPayload(BaseModel):
    """
    Payload schema for reporting complete scan results back to the API.
    """
    agent_id: str
    scan_id: str
    started_at: datetime
    finished_at: datetime
    hosts: List[HostInfo] = Field(default_factory=list)
    vulnerabilities: List[VulnerabilityReport] = Field(default_factory=list)
