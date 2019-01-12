from behave import given, when, then


@given('a newly created bank account "9890"')
def create_bank_account(context):
    pass  # Intentionally blank


# @when('I deposit the account "{account_number}" with "{amount}" credits')
# def deposit_to_account_number(context, account_number, amount):
#     worker = context.worker
#     event = {"accountNumber": account_number, "amount": amount}
#     worker.consumer.produce(event)
#
#
# @then(
#     'the account "{account_number}" should has "{final_balance:d}" credit(s)')  # noqa
# def assert_account_has_balance(context, account_number, final_balance):
#     balance_repository = context.balance_repository
#     assert balance_repository.fetch_by_account_number(
#         account_number)['clearedBalance'] == final_balance
#
#
# @given('my account_number is "{account_number}"')  # noqa
# def store_account_number_in_context(context, account_number):
#     context.account_number = account_number


@when('a balance update message is received for account "{account_number}" with {amount:d} credits')  # noqa
def deposit_account_from_context(context, account_number, amount):
    worker = context.worker
    event = {"accountNumber": account_number, "balance": amount}
    worker.consumer.produce(event)


@then('the account "{account_number}" should have {final_balance:d} credits')
def assert_balance_from_context(context, account_number, final_balance):
    balance_repository = context.balance_repository
    assert balance_repository.fetch_by_account_number(
        account_number)['clearedBalance'] == final_balance
