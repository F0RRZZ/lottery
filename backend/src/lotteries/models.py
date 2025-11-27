import enum

from sqlalchemy import ARRAY
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.core.models import TimestampMixin
from src.database import Base


class LotteryType(enum.Enum):
    BIG = 'big'
    SMALL = 'small'


class Lottery(TimestampMixin, Base):
    __tablename__ = 'lotteries'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=500))
    start_at: Mapped[DateTime] = mapped_column(DateTime)
    ended_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    numbers: Mapped[list[int]] = mapped_column(
        ARRAY(Integer, dimensions=1), nullable=False,
    )
    task_id: Mapped[str] = mapped_column(String(length=32), nullable=True)
    preview_big: Mapped[str] = mapped_column(String(length=500), nullable=True)
    preview_small: Mapped[str] = mapped_column(
        String(length=500),
        nullable=True,
    )
    lottery_type: Mapped[LotteryType] = mapped_column(
        Enum(LotteryType, name='lotterytype', create_type=True),
        default=LotteryType.SMALL,
        nullable=False,
    )

    tickets = relationship(
        'Ticket', back_populates='lottery',
    )
