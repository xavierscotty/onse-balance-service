import pytest
from balance_service.worker.model.balance_calculator import BalanceCalculator


@pytest.fixture
def calculator():
    return BalanceCalculator(10)


def test_debit_should_increase_assets(calculator):
    balance = calculator.calculate(3)
    assert balance == 13


def test_credit_should_decrease_assets(calculator):
    balance = calculator.calculate(-4)
    assert balance == 6
