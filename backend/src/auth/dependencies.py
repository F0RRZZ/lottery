from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from src.auth.repositories import UserRepository
from src.auth.service import AuthService
from src.database import get_db


async def get_auth_service(
    db: Annotated[AsyncSession, Depends(get_db)],
) -> AuthService:
    user_repo = UserRepository(db)
    return AuthService(user_repo)


async def get_current_user_dependency(
    token: Annotated[str, Depends(AuthService.oauth2_scheme)],
    auth_service: AuthService = Depends(get_auth_service),
) -> User:
    return await auth_service.get_current_user(token)
