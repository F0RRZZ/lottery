from typing import Any, Dict, List, Literal

from fastapi import HTTPException
from fastapi import status
from taskiq_redis.exceptions import ResultIsMissingError

from src.lotteries.models import Lottery
from src.lotteries.repository import LotteryRepository
from src.lotteries.schemas import LotteryCreate
from src.lotteries.schemas import LotteryResponse
from src.lotteries.schemas import LotteryUpdate
from src.lotteries.tasks import run_lottery
from src.task_app import broker


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

    async def update_lottery(
        self,
        lottery_id: int,
        lottery_data: LotteryUpdate,
    ) -> LotteryResponse:
        await self._get_lottery_or_404(lottery_id)
        updated_lottery = await self.lotteries_repo.update_lottery(
            lottery_id,
            lottery_data,
        )
        return LotteryResponse.model_validate(
            updated_lottery,
            from_attributes=True,
        )

    async def delete_lottery(self, lottery_id: int) -> None:
        lottery = await self._get_lottery_or_404(lottery_id)
        return await self.lotteries_repo.delete_lottery(lottery)

    async def start_lottery(
        self,
        lottery_id: int,
    ) -> Dict[Literal['task_id'], str]:
        lottery = await self._get_lottery_or_404(lottery_id)
        task = await run_lottery.kiq(lottery_id)

        lottery.task_id = task.task_id
        await self.lotteries_repo.session.commit()
        await self.lotteries_repo.session.refresh(lottery)

        return {'task_id': task.task_id}

    async def check_lottery_status(
        self,
        lottery_id: int,
        task_id: str,
    ) -> Dict[str, Any]:
        try:
            result = await broker.result_backend.get_result(task_id)
        except ResultIsMissingError:
            result = None

        lottery = await self._get_lottery_or_404(lottery_id)
        response = {
            'status': 'completed',
            'task_id': task_id,
            'result': None,
            'numbers': lottery.numbers if lottery else [],
        }

        if result is None:
            response.update({'status': 'pending'})
        elif result.is_err:
            response.update({'status': 'failed', 'error': str(result.error)})
        else:
            response.update({'result': result.return_value})

        return response

    async def _get_lottery_or_404(self, lottery_id: int) -> Lottery:
        lottery = await self.lotteries_repo.get_lottery(lottery_id)
        if lottery is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Lottery with id {lottery_id} is not found',
            )
        return lottery
