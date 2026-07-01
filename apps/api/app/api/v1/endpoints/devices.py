from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.schemas.host import HostOut
from app.services.host import host_service

router = APIRouter()

@router.get("/", response_model=List[HostOut])
async def read_hosts(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
) -> List[HostOut]:
    """
    Retrieve inventory of scanned hosts.
    """
    hosts = await host_service.list_hosts(db, skip=skip, limit=limit)
    return [HostOut.model_validate(h) for h in hosts]
