from typing import Annotated, Any, Dict, List, Literal

from fastapi import APIRouter
from fastapi import Depends

from src.lotteries.dependencies import get_lotteries_service
from src.lotteries.schemas import LotteryCreate
from src.lotteries.schemas import LotteryResponse
from src.lotteries.schemas import LotteryUpdate
from src.lotteries.service import LotteryService

router = APIRouter(
    prefix='/api/lottery',
    tags=['lottery'],
)


@router.get('/')
async def get_lotteries_list(
    lotteries_service: Annotated[
        LotteryService,
        Depends(get_lotteries_service),
    ],
) -> List[LotteryResponse]:
    return await lotteries_service.get_lotteries_list()


@router.get('/{lottery_id}')
async def get_lottery(
    lottery_id: int,
    lotteries_service: Annotated[
        LotteryService,
        Depends(get_lotteries_service),
    ],
) -> LotteryResponse:
    return await lotteries_service.get_lottery(lottery_id)


@router.post('/')
async def create_lottery(
    lottery: LotteryCreate,
    lotteries_service: Annotated[
        LotteryService,
        Depends(get_lotteries_service),
    ],
) -> LotteryResponse:
    return await lotteries_service.create_lottery(lottery)


@router.put('/{lottery_id}')
async def update_lottery(
    lottery_id: int,
    lottery_data: LotteryUpdate,
    lotteries_service: Annotated[
        LotteryService,
        Depends(get_lotteries_service),
    ],
) -> LotteryResponse:
    return await lotteries_service.update_lottery(
        lottery_id,
        lottery_data,
    )


@router.delete('/{lottery_id}')
async def delete_lottery(
    lottery_id: int,
    lotteries_service: Annotated[
        LotteryService,
        Depends(get_lotteries_service),
    ],
) -> None:
    return await lotteries_service.delete_lottery(lottery_id)


@router.post('/{lottery_id}/start')
async def start_lottery(
    lottery_id: int,
    lotteries_service: Annotated[
        LotteryService,
        Depends(get_lotteries_service),
    ],
) -> Dict[Literal['task_id'], str]:
    return await lotteries_service.start_lottery(lottery_id)


@router.get('/{lottery_id}/status/{task_id}/')
async def lottery_status(
    lottery_id: int,
    task_id: str,
    lotteries_service: Annotated[
        LotteryService,
        Depends(get_lotteries_service),
    ],
) -> Dict[str, Any]:
    return await lotteries_service.check_lottery_status(lottery_id, task_id)
