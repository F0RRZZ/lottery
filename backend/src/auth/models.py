from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from core.database import Base
from core.database import utc_now


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False,
    )
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    surname: Mapped[str] = mapped_column(String(100), nullable=False)
    patronymic: Mapped[str] = mapped_column(String(100), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=utc_now,
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime, default=utc_now, onupdate=utc_now,
    )

    def __repr__(self):
        return (
            f'User(id={self.id}, username={self.username}, email={self.email})'
        )
