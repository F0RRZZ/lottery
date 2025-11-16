from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.auth.models import User
from src.auth.schemas import CreateUser
from src.auth.utils import get_password_hash
from src.auth.utils import verify_password


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_username(self, username: str) -> Optional[User]:
        result = await self.session.execute(
            select(User).where(User.username == username),
        )
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> Optional[User]:
        result = await self.session.execute(
            select(User).where(User.email == email),
        )
        return result.scalar_one_or_none()

    async def create_user(self, user_data: CreateUser) -> User:
        hashed_password = get_password_hash(user_data.password)

        user = User(
            username=user_data.username,
            email=user_data.email,
            password=hashed_password,
            name=user_data.name,
            surname=user_data.surname,
            patronymic=user_data.patronymic,
        )

        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user

    async def authenticate_user(
        self, username: str, password: str,
    ) -> Optional[User]:
        user: Optional[User] = await self.session.scalar(
            select(User).where(User.username == username),
        )
        if not user or not verify_password(password, user.password):
            return None
        return user
