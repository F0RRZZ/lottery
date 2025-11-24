from pathlib import Path
from typing import Optional

from pydantic import computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict
import redis

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / '.env',
        env_ignore_empty=True,
    )

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    ALGORITHM: str = 'HS256'
    SECRET_KEY: str = 'dummy-key'

    DB_HOST: str = 'db'
    DB_PASSWORD: str = 'lottery'
    DB_PORT: int = 5432
    DB_NAME: str = 'lottery'
    DB_USER: str = 'lottery'

    REDIS_HOST: str = 'lottery_redis'
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: Optional[str] = None

    RABBITMQ_HOST: str = 'rabbitmq'
    RABBITMQ_PORT: int = 5672
    RABBITMQ_USER: str = 'guest'
    RABBITMQ_PASSWORD: str = 'guest'

    @computed_field
    @property
    def ASYNC_DATABASE_URL(self) -> str:
        return str(
            MultiHostUrl.build(
                scheme='postgresql+asyncpg',
                username=self.DB_USER,
                password=self.DB_PASSWORD,
                host=self.DB_HOST,
                port=self.DB_PORT,
                path=self.DB_NAME,
            ),
        )

    @computed_field
    @property
    def RABBITMQ_URL(self) -> str:
        return str(
            MultiHostUrl.build(
                scheme='amqp',
                username=self.RABBITMQ_USER,
                password=self.RABBITMQ_PASSWORD,
                host=self.RABBITMQ_HOST,
                port=self.RABBITMQ_PORT,
            ),
        )

    @computed_field
    @property
    def REDIS_URL(self) -> str:
        return str(
            MultiHostUrl.build(
                scheme='redis',
                host=self.REDIS_HOST,
                port=self.REDIS_PORT,
            ),
        )


settings = Settings()

redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=0,
    password=settings.REDIS_PASSWORD,
    decode_responses=True,
)
