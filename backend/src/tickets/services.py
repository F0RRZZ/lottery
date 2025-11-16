import hashlib
import itertools
import random
from typing import List, Optional, Self, TypeAlias

from src.tickets import exceptions

Ticket: TypeAlias = list[list[list[Optional[int]]]]


class TicketGenerator:
    MAX_ATTEMPTS = 100

    def __init__(self, tickets_count: Optional[int] = None) -> None:
        if tickets_count > 1_000_000:
            raise exceptions.TicketsCountExceedError
        self.limit = tickets_count
        self.tickets_generated = 0
        self.all_row_patterns = list(itertools.combinations(range(9), 5))
        self.generated_hashes: set[str] = set()

    def __iter__(self) -> Self:
        if not self.limit:
            raise exceptions.TicketsCountNotSetError
        self.tickets_generated = 0
        return self

    def __next__(self) -> Ticket:
        if self.limit < self.tickets_generated:
            self.tickets_generated += 1
            return self.generate_ticket()
        raise StopIteration

    def generate_ticket(self) -> Ticket:
        for _ in range(self.MAX_ATTEMPTS):
            ticket = self._generate_ticket_with_sections()
            ticket_hash = self._get_ticket_hash(ticket)

            if ticket_hash not in self.generated_hashes:
                self.generated_hashes.add(ticket_hash)
                return ticket
        raise exceptions.UniqueTicketGenerationError(self.MAX_ATTEMPTS)

    def _generate_ticket_with_sections(self) -> Ticket:
        ticket: Ticket = []

        for _ in range(2):
            patterns = random.sample(self.all_row_patterns, 3)
            numbers = random.sample(range(1, 91), 15)
            numbers_iter = iter(numbers)

            section = []
            for pattern in patterns:
                row = [None] * 9
                for pos in pattern:
                    row[pos] = next(numbers_iter)
                section.append(row)

            ticket.append(section)

        return ticket

    def _get_ticket_hash(self, ticket: Ticket) -> str:  # noqa: CCR001
        flat_ticket_cells = []
        for section in ticket:
            for row in section:
                for cell in row:
                    flat_ticket_cells.append(
                        str(cell) if cell else 'NULL',
                    )
        ticket_cells_string = '|'.join(flat_ticket_cells)
        return hashlib.md5(ticket_cells_string.encode()).hexdigest()

    def generate_mass_tickets(self, tickets_count: int) -> List[Ticket]:
        if tickets_count > 1_000_000:
            raise exceptions.TicketsCountExceedError
        tickets = []
        for _ in range(tickets_count):
            tickets.append(self.generate_ticket())
        return tickets
