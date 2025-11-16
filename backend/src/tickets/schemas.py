from typing import List, Optional

from pydantic import BaseModel

from src.auth.schemas import UserResponse


class TicketResponse(BaseModel):
    id: int
    user_id: UserResponse
    lottery_id: int
    numbers: List[List[Optional[int]]]


class TicketCreate(BaseModel):
    lottery_id: int
