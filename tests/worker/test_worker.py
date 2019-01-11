from unittest.mock import Mock
import json
import pytest

from balance_service.worker.worker import Worker
from balance_service.worker.mock.mock_rabbit_events import MockEvents
from balance_service.mocks.mock_balance_repository import MockBalanceRepository
from balance_service.worker.config import config


@pytest.fixture(scope='function')
def worker(balance, logger):
    worker = Worker(consumer=MockEvents(),
                         balance=balance,
                         config=config,
                         logger=logger)
    worker.start()
    return worker


@pytest.fixture(scope='function')
def balance():
    return MockBalanceRepository()


@pytest.fixture(scope='function')
def logger():
    return Mock()


def test_a_message_is_logged_on_start(worker, logger, balance):
    worker.start()
    logger.info.assert_called_with(
        f'Worker -{config.APP_NAME}- starts event processing')


def test_a_message_is_logged_on_event(worker, logger, balance):
    event = {'accountNumber': '1234', 'amount': 99}
    worker.consumer.produce(event)
    logger.debug.assert_called_with(
        'Successfulty sync balance:', process_event='update-balance')


def test_the_worker_should_updates_balance(worker, logger, balance):
    event_v1 = {"accountNumber": "1234", "amount": "1"}
    event_v2 = {"accountNumber": "1234", "amount": "3"}
    final_balance = 4
    worker.consumer.produce(event_v1)
    worker.consumer.produce(event_v2)
    assert balance.fetch_by_account_number(
        "1234")['clearedBalance'] == final_balance


def test_the_worker_should_not_updates_balance(worker, logger, balance):
    account_number = '12340'
    event_v1 = {"accountNumber": account_number, "amount": "1"}
    event_v2 = {"accountNumber": "12370", "amount": "3"}
    final_balance = 1
    worker.consumer.produce(event_v1)
    worker.consumer.produce(event_v2)
    assert balance.fetch_by_account_number(
        account_number)['clearedBalance'] == final_balance


def test_the_worker_should_support_negative_balance(worker, logger, balance):
    account_number = '12340'
    event_v1 = {"accountNumber": account_number, "amount": "1"}
    event_v2 = {"accountNumber": account_number, "amount": "-3"}
    final_balance = -2
    worker.consumer.produce(event_v1)
    worker.consumer.produce(event_v2)
    assert balance.fetch_by_account_number(
        account_number)['clearedBalance'] == final_balance
