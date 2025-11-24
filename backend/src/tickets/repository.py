from collections.abc import Sequence
from typing import Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.auth.models import User
from src.tickets.models import Ticket
from src.tickets.schemas import TicketCreate
from src.tickets.ticket_generator import TicketGenerator


class TicketRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_tickets_list(
        self,
        lottery_id: Optional[int] = None,
        user_id: Optional[int] = None,
    ) -> Sequence[Ticket]:
        query = select(Ticket)

        if lottery_id:
            query = query.filter(Ticket.lottery_id == lottery_id)

        if user_id:
            query = query.filter(Ticket.user_id == user_id)

        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_ticket(self, user: User, ticket_id: int) -> Optional[Ticket]:
        ticket = await self.session.execute(
            select(Ticket).where(
                Ticket.id == ticket_id,
                Ticket.user_id == user.id,
            ),
        )
        return ticket.scalar_one_or_none()

    async def create_ticket(
        self,
        user: User,
        ticket_data: TicketCreate,
    ) -> Ticket:
        ticket = Ticket(
            lottery_id=ticket_data.lottery_id,
            user_id=user.id,
            numbers=TicketGenerator().generate_ticket(),
        )

        self.session.add(ticket)
        await self.session.commit()
        await self.session.refresh(ticket)

        return ticket

    async def delete_ticket(self, ticket: Union[int, Ticket]) -> None:
        if isinstance(ticket, int):
            if ticket_for_delete := await self.get_ticket(ticket):
                await self.session.delete(ticket_for_delete)
        elif isinstance(ticket, Ticket):
            await self.session.delete(ticket)
        await self.session.commit()
