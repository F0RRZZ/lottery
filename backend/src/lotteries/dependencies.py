from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.lotteries.repository import LotteryRepository
from src.lotteries.service import LotteryService


async def get_lotteries_service(
    db: Annotated[AsyncSession, Depends(get_db)],
):
    lotteries_repo = LotteryRepository(db)
    return LotteryService(lotteries_repo)
