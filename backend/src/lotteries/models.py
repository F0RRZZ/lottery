from sqlalchemy import ARRAY
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.core.models import TimestampMixin
from src.database import Base


class Lottery(TimestampMixin, Base):
    __tablename__ = 'lotteries'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    start_at: Mapped[DateTime] = mapped_column(DateTime)
    ended_at: Mapped[DateTime] = mapped_column(DateTime)
    numbers: Mapped[list[int]] = mapped_column(
        ARRAY(Integer, dimensions=1), nullable=False,
    )

    tickets = relationship(
        'Ticket', back_populates='lottery',
    )
