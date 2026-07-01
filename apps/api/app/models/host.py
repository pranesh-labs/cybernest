from typing import List, Optional
from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base_class import Base

class Host(Base):
    """
    SQLAlchemy Model representing scanned system hosts.
    """
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    ip: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    mac: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    hostname: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    os_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    os_version: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    open_ports: Mapped[List[int]] = mapped_column(JSON, default=list) # JSON type to hold port lists
