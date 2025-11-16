import datetime as dt
from typing import Any, Optional

from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from jose import JWTError

from src.auth.constances import CREDENTIALS_EXCEPTION
from src.auth.models import User
from src.auth.repository import UserRepository
from src.auth.schemas import CreateUser
from src.auth.schemas import TokenData
from src.auth.schemas import UserResponse
from src.config import settings


class AuthService:
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def register_user(self, user_data: CreateUser) -> UserResponse:
        existing_user = await self.user_repo.get_by_username(
            user_data.username,
        )
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Username already registered',
            )

        existing_email = await self.user_repo.get_by_email(user_data.email)
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Email already registered',
            )

        user = await self.user_repo.create_user(user_data)

        return UserResponse.model_validate(user)

    async def get_token(
        self, form_data: OAuth2PasswordRequestForm,
    ) -> dict[str, Any]:
        user = await self.user_repo.authenticate_user(
            form_data.username, form_data.password,
        )
        if not user:
            raise CREDENTIALS_EXCEPTION

        return JWTService.create_tokens(data={'sub': user.username})

    async def refresh_token(self, refresh_token: str) -> dict[str, Any]:
        payload = JWTService.verify_token(refresh_token)
        username = payload.get('sub')
        if not username:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid token',
            )

        user = await self.user_repo.get_by_username(username)

        if not user or not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='User not found or inactive',
            )

        return JWTService.create_tokens(data={'sub': user.username})

    async def get_current_user(
        self, token: str,
    ) -> User:
        token_data = self._get_token_data(token)
        user: Optional[User] = await self.user_repo.get_by_username(
            token_data.username,
        )
        if user is None:
            raise CREDENTIALS_EXCEPTION

        return user

    def _get_token_data(self, token: str) -> TokenData:
        payload = JWTService.verify_token(token)
        username: Optional[str] = payload.get('sub')
        if username is None:
            raise CREDENTIALS_EXCEPTION

        return TokenData(username=username)


class JWTService:
    @staticmethod
    def create_tokens(data: dict) -> dict[str, Any]:
        return {
            'access_token': JWTService.create_access_token(data),
            'refresh_token': JWTService.create_refresh_token(data),
            'token_type': 'bearer',
            'expires_in': settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        }

    @staticmethod
    def create_access_token(data: dict) -> str:
        to_encode = data.copy()
        expire = (
            dt.datetime.now(dt.timezone.utc) + dt.timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
            )
        )
        to_encode.update({'exp': expire})
        return jwt.encode(
            to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM,
        )

    @staticmethod
    def create_refresh_token(data: dict) -> str:
        to_encode = data.copy()
        expire = (
            dt.datetime.now(dt.timezone.utc) + dt.timedelta(
                days=settings.REFRESH_TOKEN_EXPIRE_DAYS,
            )
        )
        to_encode.update({'exp': expire, 'type': 'refresh'})
        return jwt.encode(
            to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM,
        )

    @staticmethod
    def verify_token(token: str) -> dict:
        try:
            return jwt.decode(
                token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM],
            )
        except JWTError:
            raise CREDENTIALS_EXCEPTION
