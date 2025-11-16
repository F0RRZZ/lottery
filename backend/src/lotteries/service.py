from typing import List

from fastapi import HTTPException
from fastapi import status

from src.lotteries.models import Lottery
from src.lotteries.repository import LotteryRepository
from src.lotteries.schemas import LotteryCreate
from src.lotteries.schemas import LotteryResponse


class LotteryService:
    def __init__(self, lotteries_repo: LotteryRepository) -> None:
        self.lotteries_repo = lotteries_repo

    async def get_lotteries_list(self) -> List[LotteryResponse]:
        lotteries_list = await self.lotteries_repo.get_lotteries_list()
        return [
            LotteryResponse.model_validate(lottery, from_attributes=True)
            for lottery in lotteries_list
        ]

    async def get_lottery(self, lottery_id: int) -> LotteryResponse:
        lottery = await self._get_lottery_or_404(lottery_id)
        return LotteryResponse.model_validate(lottery, from_attributes=True)

    async def create_lottery(
        self,
        lottery_data: LotteryCreate,
    ) -> LotteryResponse:
        lottery = await self.lotteries_repo.create_lottery(lottery_data)
        return LotteryResponse.model_validate(lottery, from_attributes=True)

    async def delete_lottery(self, lottery_id: int) -> None:
        lottery = await self._get_lottery_or_404(lottery_id)
        return await self.lotteries_repo.delete_lottery(lottery)

    async def _get_lottery_or_404(self, lottery_id: int) -> Lottery:
        lottery = await self.lotteries_repo.get_lottery(lottery_id)
        if lottery is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Lottery with id {lottery_id} is not found',
            )
        return lottery
