from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from shared_python.security import get_password_hash, verify_password
from app.models.user import User
from app.schemas.user import UserCreate
from app.repositories.user import user_repository

class UserService:
    async def authenticate(
        self, db: AsyncSession, *, email: str, password: str
    ) -> Optional[User]:
        user = await user_repository.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def register_user(self, db: AsyncSession, *, user_in: UserCreate) -> User:
        # Check if user already exists
        existing_user = await user_repository.get_by_email(db, email=user_in.email)
        if existing_user:
            raise ValueError("Email already registered")
        
        # Hash password and create record
        hashed_password = get_password_hash(user_in.password)
        db_obj = User(
            email=user_in.email,
            hashed_password=hashed_password,
            full_name=user_in.full_name,
            role=user_in.role or "analyst",
            is_active=True,
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

user_service = UserService()
