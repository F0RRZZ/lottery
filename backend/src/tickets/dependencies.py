from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.tickets.repository import TicketRepository
from src.tickets.service import TicketService


async def get_tickets_service(
    db: Annotated[AsyncSession, Depends(get_db)],
) -> TicketService:
    tickets_repo = TicketRepository(db)
    return TicketService(tickets_repo)
