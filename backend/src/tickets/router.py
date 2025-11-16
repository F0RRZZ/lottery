from typing import Annotated, List

from fastapi import APIRouter
from fastapi import Depends

from src.auth.dependencies import get_current_user_dependency
from src.auth.models import User
from src.tickets.dependencies import get_tickets_service
from src.tickets.schemas import TicketCreate
from src.tickets.schemas import TicketResponse
from src.tickets.service import TicketService

router = APIRouter(
    prefix='/tickets',
    tags=['tickets'],
)


@router.get('/', response_model=List[TicketResponse])
async def get_tickets_list(
    tickets_service: Annotated[TicketService, Depends(get_tickets_service)],
    user: Annotated[User, Depends(get_current_user_dependency)],
) -> List[TicketResponse]:
    return await tickets_service.get_tickets_list(user)


@router.get('/{ticket_id}')
async def get_ticket(
    ticket_id: int,
    tickets_service: Annotated[TicketService, Depends(get_tickets_service)],
    user: Annotated[User, Depends(get_current_user_dependency)],
) -> TicketResponse:
    return await tickets_service.get_ticket(user, ticket_id)


@router.post('/')
async def create_ticket(
    ticket: TicketCreate,
    tickets_service: Annotated[TicketService, Depends(get_tickets_service)],
    user: Annotated[User, Depends(get_current_user_dependency)],
) -> TicketResponse:
    return await tickets_service.create_ticket(user, ticket)


@router.delete('/{ticket_id}')
async def delete_ticket(
    ticket_id: int,
    tickets_service: Annotated[TicketService, Depends(get_tickets_service)],
    user: Annotated[User, Depends(get_current_user_dependency)],
) -> None:
    return await tickets_service.delete_ticket(user, ticket_id)
