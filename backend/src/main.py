from contextlib import asynccontextmanager
import logging
from typing import AsyncGenerator


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.auth.router import router as auth_router
from src.lotteries.router import router as lotteries_router
from src.renderers import MsgSpecJSONResponse
from src.task_app import broker
from src.tickets.router import router as tickets_router

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    if not broker.is_worker_process:
        await broker.startup()
    logger.info('Broker started successfully')

    yield

    if not broker.is_worker_process:
        await broker.shutdown()
    logger.info('Broker shutdown successfully')


app = FastAPI(
    title='Lottery project',
    description='Lottery project API',
    version='1.0.0',
    default_response_class=MsgSpecJSONResponse,
    lifespan=lifespan,
)
app.include_router(auth_router)
app.include_router(tickets_router)
app.include_router(lotteries_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/health-check')
async def health_check():
    return {'status': 'OK'}
