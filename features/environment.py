import logging

from structlog import wrap_logger

from balance_service.app import app
from balance_service.mocks.mock_balance_repository import MockBalanceRepository
from balance_service.worker.mock.mock_rabbit_events import MockEvents
from balance_service.worker.worker import Worker


def before_feature(context, feature):
    if 'app' in feature.tags:
        before_app_feature(context)
    elif 'worker' in feature.tags:
        before_worker_feature(context)
    else:
        raise Exception


def before_app_feature(context):
    from balance_service.app import config
    balance_repository = MockBalanceRepository()
    application = app.create(config=config.test_config,
                             repository=balance_repository)
    context.web_client = application.test_client()
    context.balance_repository = balance_repository


def before_worker_feature(context):
    from balance_service.worker.config import config
    balance_repository = MockBalanceRepository()
    logger = logging.getLogger()
    logger.addHandler(logging.NullHandler())
    worker = Worker(consumer=MockEvents(),
                    balance=balance_repository,
                    config=config,
                    logger=wrap_logger(logger))
    context.worker = worker
    context.balance_repository = balance_repository
    context.logger = logger

    worker.start()
