from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from src.tickets.schemas import TicketResponse


class LotteryResponse(BaseModel):
    id: int
    name: str
    tickets: List[TicketResponse]
    start_at: datetime
    ended_at: Optional[datetime]
    numbers: List[int]


class LotteryCreate(BaseModel):
    name: str
    start_at: datetime
