import pytest

from balance_service.app import config
from balance_service.app.app import create
from balance_service.mocks.mock_balance_repository import MockBalanceRepository


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
