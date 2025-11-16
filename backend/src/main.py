from fastapi import FastAPI

from src.auth.router import router as auth_router
from src.lotteries.router import router as lotteries_router
from src.renderers import MsgSpecJSONResponse
from src.tickets.router import router as tickets_router

app = FastAPI(
    title='Lottery project',
    description='Lottery project API',
    version='1.0.0',
    default_response_class=MsgSpecJSONResponse,
)
app.include_router(auth_router)
app.include_router(tickets_router)
app.include_router(lotteries_router)


@app.get('/health-check')
async def health_check():
    return {'status': 'OK'}
