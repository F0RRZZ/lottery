from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.auth.dependencies import get_auth_service
from src.auth.dependencies import get_current_user_dependency
from src.auth.models import User
from src.auth.schemas import CreateUser
from src.auth.schemas import RefreshTokenRequest
from src.auth.schemas import Token
from src.auth.schemas import UserResponse
from src.auth.service import AuthService

router = APIRouter(
    prefix='/api/auth',
    tags=['auth'],
)


@router.post('/register', response_model=UserResponse)
async def register_user(
    user_data: CreateUser,
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
):
    return await auth_service.register_user(user_data)


@router.post('/token', response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
):
    return await auth_service.get_token(form_data)


@router.post('/refresh', response_model=Token)
async def refresh_access_token(
    request: RefreshTokenRequest,
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
):
    return await auth_service.refresh_token(request.refresh_token)


@router.get('/me', response_model=UserResponse)
async def get_current_user_info(
    current_user: Annotated[User, Depends(get_current_user_dependency)],
):
    return UserResponse.model_validate(current_user)
