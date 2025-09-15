from typing import Optional

from sqlalchemy import ARRAY
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.core.models import TimestampMixin
from src.database import Base


class Ticket(TimestampMixin, Base):
    __tablename__ = 'tickets'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='SET NULL'))
    lottery_id: Mapped[int] = mapped_column(ForeignKey('lotteries.id', ondelete='SET NULL'))
    numbers: Mapped[list[list[Optional[int]]]] = mapped_column(
        ARRAY(Integer, dimensions=2), nullable=False,
    )

    user: Mapped['User'] = relationship('User', back_populates='tickets')
    lottery: Mapped['Lottery'] = relationship('Lottery', back_populates='tickets')
