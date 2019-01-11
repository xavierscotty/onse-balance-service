import json

from balance_service.app import app
from balance_service.app import config
from balance_service.app.mock.mock_balance_repository import MockBalanceRepository


def before_all(context):
    balance_repository = MockBalanceRepository()
    application = app.create(config=config.test_config,
                             repository=balance_repository)
    context.web_client = application.test_client()
    context.balance_repository = balance_repository
