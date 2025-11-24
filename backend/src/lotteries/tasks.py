import asyncio
from collections.abc import Sequence
import logging
import random
from typing import List, Optional

from src.database import get_db
from src.lotteries.repository import LotteryRepository
from src.lotteries.schemas import LotteryUpdate
from src.task_app import broker
from src.tickets.models import Ticket
from src.tickets.repository import TicketRepository
from src.tickets.schemas import TicketResponse

logger = logging.getLogger(__name__)


@broker.task
async def run_lottery(lottery_id: int) -> TicketResponse:  # noqa: CCR001
    gen = get_db()
    session = await anext(gen)

    lottery_repo = LotteryRepository(session)
    lottery = await lottery_repo.get_lottery(lottery_id)

    ticket_repo = TicketRepository(session)
    tickets: Sequence[Ticket] = await ticket_repo.get_tickets_list(
        lottery_id=lottery.id,
    )
    tickets = list(tickets)
    winner: Optional[Ticket] = None

    if not tickets:
        return []

    numbers = list(range(100))
    played_numbers: List[int] = []

    for _ in range(100):
        number: int = random.choice(numbers)
        played_numbers.append(numbers.pop(numbers.index(number)))

        if len(played_numbers) >= 30:
            for ticket in tickets:
                if _is_ticket_win(played_numbers, ticket):
                    winner = ticket
                    break

        await lottery_repo.update_lottery(
            lottery.id,
            LotteryUpdate(numbers=played_numbers),
        )

        if winner:
            break

        await asyncio.sleep(3)

    winner.status = 'WIN'
    await session.commit()
    await session.refresh(winner)

    for ticket in tickets:
        if ticket.id != winner.id:
            ticket.status = 'LOSE'
            await session.commit()
            await session.refresh(ticket)

    return TicketResponse.model_validate(winner, from_attributes=True)


def _is_ticket_win(  # noqa: CCR001
    played_numbers: List[int],
    ticket: Ticket,
) -> bool:
    ticket_numbers = []
    for nums_part in ticket.numbers:
        for row in nums_part:
            for num in row:
                if num is not None:
                    ticket_numbers.append(num)

    return all(num in played_numbers for num in ticket_numbers)
