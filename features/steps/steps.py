import json
from http import HTTPStatus

@given(u'a bank account "{account_number}" with balance "{cleared_balance:d}"')
def step_impl(context, account_number, cleared_balance):
    account_data = {
        'accountNumber': account_number,
        'clearedBalance': cleared_balance
    }
    context.balance_repository.store(account_number, json.dumps(account_data))

@when(u'I request the account "{account_number}" balance')
def step_impl(context, account_number):
    response = context.web_client.get(f'/balance/{account_number}')
    context.response = response


@then(u'the account balance should be "{cleared_balance:d}"')
def step_impl(context, cleared_balance):
    response = context.response.get_json()
    print(response['clearedBalance'])
    assert response['clearedBalance']
    assert response['clearedBalance'] == cleared_balance


@then(u'the account data not found')
def step_impl(context):
    response = context.response
    status_code = response.status_code
    assert status_code == HTTPStatus.NOT_FOUND, f'Expected status code to be {HTTPStatus.NOT_FOUND}; got {status_code}'
