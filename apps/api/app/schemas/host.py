from typing import List, Optional
from pydantic import BaseModel

class HostBase(BaseModel):
    ip: str
    mac: Optional[str] = None
    hostname: Optional[str] = None
    os_name: Optional[str] = None
    os_version: Optional[str] = None
    open_ports: List[int] = []

class HostCreate(HostBase):
    pass

class HostUpdate(BaseModel):
    ip: Optional[str] = None
    mac: Optional[str] = None
    hostname: Optional[str] = None
    os_name: Optional[str] = None
    os_version: Optional[str] = None
    open_ports: Optional[List[int]] = None

class HostInDBBase(HostBase):
    id: int

    class Config:
        from_attributes = True

class HostOut(HostInDBBase):
    pass
