import pytest, json
from balance_service.app.infrastructure.balance_repository import AccountNotFound

def test_store_contains_account_data(balance_repository):
    account_number = '99999'
    account_data = {
        'accountNumber': account_number,
        'clearedBalance': 4231
    }
    balance_repository.store(account_number, json.dumps(account_data))
    result = balance_repository.fetch_by_account_number(account_number)
    assert result == str(json.dumps(account_data))


def test_store_contains_no_account_data(balance_repository):
    account_number = '99999'
    account_data = {
        'accountNumber': account_number,
        'clearedBalance': 4231
    }
    other_account_number = '0000000'
    balance_repository.store(account_number, json.dumps(account_data))
    with pytest.raises(AccountNotFound):
        balance_repository.fetch_by_account_number(other_account_number)
