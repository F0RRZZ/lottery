import datetime as dt
from typing import Any, Optional

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.auth.constances import CREDENTIALS_EXCEPTION
from src.auth.models import User
from src.auth.schemas import TokenData
from src.config import settings
from src.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


class JWTService:
    def create_tokens(self, data: dict) -> dict[str, Any]:
        return {
            'access_token': self.create_access_token(data),
            'refresh_token': self.create_refresh_token(data),
            'token_type': 'bearer',
            'expires_in': settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        }

    def create_access_token(self, data: dict) -> str:
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

    def create_refresh_token(self, data: dict) -> str:
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

    def verify_token(self, token: str) -> dict:
        try:
            return jwt.decode(
                token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM],
            )
        except JWTError:
            raise CREDENTIALS_EXCEPTION

    async def get_current_user(
        self,
        token: str = Depends(oauth2_scheme),
        db: AsyncSession = Depends(get_db),
    ) -> User:
        token_data = self._get_token_data(token)
        user: Optional[User] = await db.scalar(
            select(User).where(User.username == token_data.username),
        )
        if user is None:
            raise CREDENTIALS_EXCEPTION

        return user

    def _get_token_data(self, token: str) -> TokenData:
        payload = self.verify_token(token)
        username: Optional[str] = payload.get('sub')
        if username is None:
            raise CREDENTIALS_EXCEPTION

        return TokenData(username=username)
