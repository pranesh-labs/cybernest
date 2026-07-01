from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base_class import Base

class User(Base):
    """
    SQLAlchemy Model for system users.
    """
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    role: Mapped[str] = mapped_column(String(50), default="analyst")
