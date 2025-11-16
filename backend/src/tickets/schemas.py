from typing import Any, List

from pydantic import BaseModel

from src.auth.schemas import UserResponse


class TicketResponse(BaseModel):
    id: int
    user: UserResponse
    lottery_id: int
    numbers: List[Any]


class TicketCreate(BaseModel):
    lottery_id: int
