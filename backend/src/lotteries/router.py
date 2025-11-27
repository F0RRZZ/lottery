import base64
from pathlib import Path
from typing import Annotated, Any, Dict, List, Literal
import uuid

from fastapi import APIRouter
from fastapi import Depends

from src.config import settings
from src.lotteries.dependencies import get_lotteries_service
from src.lotteries.schemas import LotteryCreate
from src.lotteries.schemas import LotteryResponse
from src.lotteries.schemas import LotteryResponseAfterCreate
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
) -> LotteryResponseAfterCreate:
    big_path = None
    small_path = None

    media_dir = Path(__file__).parent.parent.parent / 'media' / 'uploads'

    if lottery.preview_big:
        file_extension = lottery.preview_big.split(';')[0].split('/')[1]
        filename = f'{uuid.uuid4()}.{file_extension}'
        big_path = f'{settings.MEDIA_URL}/{filename}'

        image_data = base64.b64decode(lottery.preview_big.split(',')[1])
        with open(media_dir / filename, 'wb') as f:
            f.write(image_data)

    if lottery.preview_small:
        file_extension = lottery.preview_small.split(';')[0].split('/')[1]
        filename = f'{uuid.uuid4()}.{file_extension}'
        small_path = f'{settings.MEDIA_URL}/{filename}'

        image_data = base64.b64decode(lottery.preview_small.split(',')[1])
        with open(media_dir / filename, 'wb') as f:
            f.write(image_data)

    lottery_data = lottery.model_dump()
    lottery_data['preview_big'] = str(big_path) if big_path else None
    lottery_data['preview_small'] = str(small_path) if small_path else None

    return await lotteries_service.create_lottery(
        LotteryCreate.model_validate(lottery_data),
    )


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
