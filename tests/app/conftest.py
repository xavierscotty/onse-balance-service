import pytest
from flask import Flask

from balance_service.app.controllers.heatlh import health
from balance_service.app.controllers.balance import balance
from balance_service.app.mock.mock_balance_repository import MockBalanceRepository
from balance_service.app.app import create
from balance_service.app import config

@pytest.fixture
def balance_repository():
    return MockBalanceRepository()


@pytest.fixture
def app(balance_repository):
    app = create(config.config, repository=balance_repository)
    return app


@pytest.fixture
def web_client(app):
    return app.test_client()
