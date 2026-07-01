from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.host import Host
from app.schemas.host import HostCreate, HostUpdate
from app.repositories.base import CRUDBase

class CRUDHost(CRUDBase[Host, HostCreate, HostUpdate]):
    async def get_by_ip(self, db: AsyncSession, *, ip: str) -> Optional[Host]:
        """
        Get scanned host by IP address.
        """
        result = await db.execute(select(self.model).filter(self.model.ip == ip))
        return result.scalars().first()

    async def get_by_mac(self, db: AsyncSession, *, mac: str) -> Optional[Host]:
        """
        Get scanned host by MAC address.
        """
        result = await db.execute(select(self.model).filter(self.model.mac == mac))
        return result.scalars().first()

host_repository = CRUDHost(Host)
