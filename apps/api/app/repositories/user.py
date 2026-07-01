from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.repositories.base import CRUDBase

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    async def get_by_email(self, db: AsyncSession, *, email: str) -> Optional[User]:
        """
        Get user by email.
        """
        result = await db.execute(select(self.model).filter(self.model.email == email))
        return result.scalars().first()

user_repository = CRUDUser(User)
