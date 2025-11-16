from typing import List

from fastapi import HTTPException
from fastapi import status
from sqlalchemy.exc import IntegrityError

from src.auth.models import User
from src.tickets.repository import TicketRepository
from src.tickets.schemas import TicketCreate
from src.tickets.schemas import TicketResponse


class TicketService:
    def __init__(self, tickets_repo: TicketRepository) -> None:
        self.tickets_repo = tickets_repo

    async def get_tickets_list(self, user: User) -> List[TicketResponse]:
        tickets = await self.tickets_repo.get_tickets_list(user)
        return [TicketResponse.model_validate(ticket) for ticket in tickets]

    async def get_ticket(self, user: User, ticket_id: int) -> TicketResponse:
        ticket = await self.tickets_repo.get_ticket(user, ticket_id)
        if ticket is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Ticket with id {ticket_id} is not found',
            )
        return TicketResponse.model_validate(ticket)

    async def create_ticket(
        self,
        user: User,
        ticket_data: TicketCreate,
    ) -> TicketResponse:
        try:
            ticket = await self.tickets_repo.create_ticket(user, ticket_data)
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Invalid user or lottery id',
            )
        return TicketResponse.model_validate(ticket)

    async def delete_ticket(self, user: User, ticket_id: int) -> None:
        ticket = await self.tickets_repo.get_ticket(user, ticket_id)
        if ticket is None or ticket.user_id != user.id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Ticket with id {ticket_id} is not found',
            )
        return await self.tickets_repo.delete_ticket(ticket)
