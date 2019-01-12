from http import HTTPStatus

from behave import given, when, then


@given('a bank account "{account_number}" with balance "{cleared_balance:d}"')
def create_account(context, account_number, cleared_balance):
    account_data = {
        "accountNumber": account_number,
        "clearedBalance": cleared_balance
    }
    context.balance_repository.store(account_number, account_data)


@when('I request the account "{account_number}" balance')
def request_account(context, account_number):
    response = context.web_client.get(f'/balance/{account_number}')
    context.response = response


@then('the account balance should be "{cleared_balance:d}"')
def assert_balance(context, cleared_balance):
    response = context.response.get_json()
    assert response['clearedBalance']
    assert response['clearedBalance'] == cleared_balance


@then('the account data not found')
def assert_not_found_response(context):
    response = context.response
    status_code = response.status_code
    assert status_code == HTTPStatus.NOT_FOUND,\
        f'Expected status code to be {HTTPStatus.NOT_FOUND}; got {status_code}'
