from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.constances import CREDENTIALS_EXCEPTION
from src.auth.repositories import UserRepository
from src.auth.schemas import CreateUser
from src.auth.schemas import RefreshTokenRequest
from src.auth.schemas import Token
from src.auth.schemas import UserResponse
from src.auth.service import JWTService
from src.database import get_db

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.post('/register', response_model=UserResponse)
async def register_user(
    user_data: CreateUser,
    db: AsyncSession = Depends(get_db),
):
    user_repo = UserRepository(db)
    existing_user = await user_repo.get_by_username(user_data.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Username already registered',
        )

    existing_email = await user_repo.get_by_email(user_data.email)
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Email already registered',
        )

    user_dict = user_data.model_dump()
    user = await user_repo.create_user(user_dict)

    return UserResponse.model_validate(user)


@router.post('/token', response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    user_repo = UserRepository(db)
    user = await user_repo.authenticate_user(
        form_data.username, form_data.password,
    )
    if not user:
        raise CREDENTIALS_EXCEPTION

    jwt_service = JWTService()
    return jwt_service.create_tokens(data={'sub': user.username})


@router.post('/refresh', response_model=Token)
async def refresh_access_token(
    request: RefreshTokenRequest,
    db: AsyncSession = Depends(get_db),
):
    jwt_service = JWTService()

    payload = jwt_service.verify_token(request.refresh_token)
    username = payload.get('sub')
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid token',
        )

    user_repo = UserRepository(db)
    user = await user_repo.get_by_username(username)

    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User not found or inactive',
        )

    return jwt_service.create_tokens(data={'sub': user.username})
