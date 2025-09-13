from pathlib import Path

from pydantic import computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

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

    RABBITMQ_DEFAULT_USER: str = 'guest'
    RABBITMQ_DEFAULT_PASS: str = 'guest'

    REDIS_HOST: str = 'lottery_redis'

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


settings = Settings()
