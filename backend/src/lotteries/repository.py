from collections.abc import Sequence
from typing import Optional, Tuple, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from sqlalchemy.sql.selectable import Select

from src.lotteries.models import Lottery
from src.lotteries.schemas import LotteryCreate
from src.lotteries.schemas import LotteryUpdate
from src.tickets.models import Ticket


class LotteryRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_lotteries_list(self) -> Sequence[Lottery]:
        result = await self.session.execute(self._get_joined_lottery_qs())
        return result.unique().scalars().all()

    async def get_lottery(self, lottery_id: int) -> Optional[Lottery]:
        result = await self.session.execute(
            self._get_joined_lottery_qs().where(Lottery.id == lottery_id),
        )
        return result.unique().scalar_one_or_none()

    def _get_joined_lottery_qs(self) -> Select[Tuple[Lottery]]:
        return select(Lottery).options(
            joinedload(Lottery.tickets).selectinload(Ticket.user),
        )

    async def create_lottery(self, lottery_data: LotteryCreate) -> Lottery:
        lottery = Lottery(
            name=lottery_data.name,
            start_at=lottery_data.start_at,
            numbers=[],
            preview_big=lottery_data.preview_big,
            preview_small=lottery_data.preview_small,
        )

        self.session.add(lottery)
        await self.session.commit()
        await self.session.refresh(lottery)

        return lottery

    async def update_lottery(
        self,
        lottery_id: int,
        lottery_data: LotteryUpdate,
    ) -> Optional[Lottery]:
        lottery = await self.get_lottery(lottery_id)

        if not lottery:
            return None

        update_data = lottery_data.model_dump(
            exclude_unset=True,
            exclude_none=True,
        )
        for field, value in update_data.items():
            setattr(lottery, field, value)

        await self.session.commit()
        await self.session.refresh(lottery)
        return lottery

    async def delete_lottery(self, lottery: Union[int, Lottery]) -> None:
        if isinstance(lottery, int):
            if lottery_for_delete := await self.get_lottery(lottery):
                await self.session.delete(lottery_for_delete)
        elif isinstance(lottery, Lottery):
            await self.session.delete(lottery)
        await self.session.commit()
