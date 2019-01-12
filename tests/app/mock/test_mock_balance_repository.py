def test_store_contains_account_data(balance_repository):
    account_number = "99999"
    account_data = {
        "accountNumber": account_number,
        "clearedBalance": 4231
    }
    balance_repository.store(account_number, account_data)
    result = balance_repository.fetch_by_account_number(account_number)
    assert result['clearedBalance'] == account_data['clearedBalance']


def test_store_contains_no_account_data(balance_repository):
    account_number = "99999"
    account_data = {
        "accountNumber": account_number,
        "clearedBalance": 4231
    }
    result = balance_repository.store(account_number, account_data)
    assert result is None
