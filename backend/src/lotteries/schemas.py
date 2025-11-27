from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel

from src.tickets.schemas import TicketResponse


class LotteryResponseAfterCreate(BaseModel):
    id: int
    name: str
    start_at: datetime
    ended_at: Optional[datetime]
    numbers: List[int]
    task_id: Optional[str]
    lottery_type: str
    preview_big: Optional[str] = None
    preview_small: Optional[str] = None


class LotteryResponse(LotteryResponseAfterCreate):
    tickets: List[TicketResponse]


class LotteryCreate(BaseModel):
    name: str
    start_at: datetime
    preview_big: Optional[str] = None
    preview_small: Optional[str] = None


class LotteryUpdate(BaseModel):
    name: Optional[str] = None
    numbers: Optional[List[Any]] = None

    class Config:
        from_attributes = True
