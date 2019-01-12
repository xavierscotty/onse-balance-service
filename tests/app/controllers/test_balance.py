from http import HTTPStatus


def test_get_balance_when_account_exists(web_client, balance_repository):
    account_number = "99999"
    account_data = {
        "accountNumber": account_number,
        "clearedBalance": 4231
    }
    expected_json = account_data
    balance_repository.store(account_number, account_data)
    response = web_client.get(f'/balance/{account_number}')
    assert response.status_code == HTTPStatus.OK
    assert response.is_json
    assert response.get_json() == expected_json


def test_get_balance_when_account_not_exists(web_client, balance_repository):
    account_number = "99999"
    account_data = {
        "accountNumber": "8907987",
        "clearedBalance": 4231
    }
    expected_json = {
        "message": "Account not found"
    }
    balance_repository.store("8907987", account_data)
    response = web_client.get(f'/balance/{account_number}')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.is_json
    assert response.get_json() == expected_json
