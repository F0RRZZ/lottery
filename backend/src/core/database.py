from datetime import datetime
from datetime import timezone

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


def utc_now():
    """Хелпер-функция для получения текущего UTC времени с timezone"""
    return datetime.now(timezone.utc)
