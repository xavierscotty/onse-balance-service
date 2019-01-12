from behave import given, when, then


@given('a newly created bank account')
def create_bank_account(context):
    worker = context.worker
    worker.start()


@when('I deposit the account "{account_number}" with "{amount}" credits')
def deposit_to_account_number(context, account_number, amount):
    worker = context.worker
    event = {"accountNumber": account_number, "amount": amount}
    worker.consumer.produce(event)


@then(
    'the account "{account_number}" should has "{final_balance:d}" credit(s)')  # noqa
def assert_account_has_balance(context, account_number, final_balance):
    balance_repository = context.balance_repository
    assert balance_repository.fetch_by_account_number(
        account_number)['clearedBalance'] == final_balance


@given(
    'I deposit and withdraw credits multiple times from account "{account_number}"')  # noqa
def deposit_and_withdraw(context, account_number):
    context.account_number = account_number


@when('I deposit the account with "{amount}" credit')
def deposit_account_from_context(context, amount):
    account_number = context.account_number
    worker = context.worker
    event = {"accountNumber": account_number, "amount": amount}
    worker.consumer.produce(event)


@when('I withdrawn from the account with "{amount}" credit')
def withdraw_from_context(context, amount):
    account_number = context.account_number
    worker = context.worker
    event = {"accountNumber": account_number, "amount": amount}
    worker.consumer.produce(event)


@then('the account should has "{final_balance:d}" credit(s)')
def assert_balance_from_context(context, final_balance):
    account_number = context.account_number
    balance_repository = context.balance_repository
    assert balance_repository.fetch_by_account_number(
        account_number)['clearedBalance'] == final_balance
