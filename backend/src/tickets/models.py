import enum
from typing import Optional

from sqlalchemy import ARRAY
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.auth.models import User
from src.core.models import TimestampMixin
from src.database import Base
from src.lotteries.models import Lottery


class TicketStatus(enum.Enum):
    NOT_PLAYED = 'not played'
    LOSE = 'lose'
    WIN = 'win'


class Ticket(TimestampMixin, Base):
    __tablename__ = 'tickets'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete='SET NULL'),
    )
    lottery_id: Mapped[int] = mapped_column(
        ForeignKey('lotteries.id', ondelete='SET NULL'),
    )
    numbers: Mapped[list[list[Optional[int]]]] = mapped_column(
        ARRAY(Integer, dimensions=2), nullable=False,
    )
    status: Mapped[TicketStatus] = mapped_column(
        Enum(TicketStatus, name='ticketstatus', create_type=True),
        default=TicketStatus.NOT_PLAYED,
        nullable=False,
    )

    user = relationship(User, back_populates='tickets')
    lottery = relationship(
        Lottery, back_populates='tickets',
    )
