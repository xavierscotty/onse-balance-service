import structlog

from balance_service.worker.config import config
from balance_service.worker.infrastructure.balance_repository import \
    BalanceRepository
from balance_service.worker.infrastructure.rabbit_events import RabbitConsumer
from balance_service.worker.worker import Worker

if __name__ == "__main__":
    logger = structlog.get_logger()
    consumer = RabbitConsumer(config, logger)
    balance = BalanceRepository(config)
    app = Worker(consumer=consumer,
                 balance=balance,
                 config=config,
                 logger=logger)
    app.start()
