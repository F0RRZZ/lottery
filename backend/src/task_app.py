from taskiq import TaskiqScheduler
from taskiq.schedule_sources import LabelScheduleSource
from taskiq_aio_pika import AioPikaBroker
from taskiq_redis import RedisAsyncResultBackend

from src.config import settings

broker = AioPikaBroker(
    settings.RABBITMQ_URL,
).with_result_backend(
    RedisAsyncResultBackend(settings.REDIS_URL),
)


scheduler = TaskiqScheduler(
    broker=broker,
    sources=[LabelScheduleSource(broker)],
)
