from typing import Any
from sqlalchemy.orm import DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    """
    SQLAlchemy 2.0 Base declarative class.
    Automatically assigns tablenames based on lowercase class name.
    """
    id: Any

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
