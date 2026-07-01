from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from shared_python.models import ScanResultPayload
from app.models.host import Host
from app.schemas.host import HostCreate, HostUpdate
from app.repositories.host import host_repository

class HostService:
    async def process_scan_payload(
        self, db: AsyncSession, *, payload: ScanResultPayload
    ) -> List[Host]:
        """
        Processes scan telemetry reported by the fingerprinting agent.
        Upserts host records based on IP/MAC address.
        """
        processed_hosts = []
        for scanned_host in payload.hosts:
            # Check by MAC first, then IP
            db_host = None
            if scanned_host.mac:
                db_host = await host_repository.get_by_mac(db, mac=scanned_host.mac)
            if not db_host:
                db_host = await host_repository.get_by_ip(db, ip=scanned_host.ip)

            if db_host:
                # Update existing record
                update_schema = HostUpdate(
                    ip=scanned_host.ip,
                    mac=scanned_host.mac,
                    hostname=scanned_host.hostname,
                    os_name=scanned_host.os_name,
                    os_version=scanned_host.os_version,
                    open_ports=scanned_host.open_ports,
                )
                db_host = await host_repository.update(db, db_obj=db_host, obj_in=update_schema)
            else:
                # Create new record
                create_schema = HostCreate(
                    ip=scanned_host.ip,
                    mac=scanned_host.mac,
                    hostname=scanned_host.hostname,
                    os_name=scanned_host.os_name,
                    os_version=scanned_host.os_version,
                    open_ports=scanned_host.open_ports,
                )
                db_host = await host_repository.create(db, obj_in=create_schema)
            
            processed_hosts.append(db_host)
        return processed_hosts

    async def list_hosts(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Host]:
        return await host_repository.get_multi(db, skip=skip, limit=limit)

host_service = HostService()
