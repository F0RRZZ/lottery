import datetime as dt
from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(
        min_length=5, max_length=50, pattern='^[a-zA-Z0-9_-]+$',
    )
    name: str = Field(min_length=1, max_length=100)
    surname: str = Field(min_length=1, max_length=100)
    patronymic: Optional[str] = Field(None, min_length=1, max_length=100)


class CreateUser(UserBase):
    password: str = Field(..., min_length=8)


class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: dt.datetime
    updated_at: dt.datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class TokenData(BaseModel):
    username: Optional[str] = None
