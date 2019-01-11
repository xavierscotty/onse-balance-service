@given(u'a newly created bank account')
def step_impl(context):
    worker = context.worker
    worker.start()


@when(u'I deposit the account "{account_number}" with "{amount}" credits')
def step_impl(context, account_number, amount):
    worker = context.worker
    event = {"accountNumber": account_number, "amount": amount}
    worker.consumer.produce(event)


@then(u'the account "{account_number}" should has "{final_balance:d}" credit(s)')
def step_impl(context, account_number, final_balance):
    balance_repository = context.balance_repository
    assert balance_repository.fetch_by_account_number(
        account_number)['clearedBalance'] == final_balance


@given(u'I deposit and withdraw credits multiple times from account "{account_number}"')
def step_impl(context, account_number):
    context.account_number = account_number


@when(u'I deposit the account with "{amount}" credit')
def step_impl(context, amount):
    account_number = context.account_number
    worker = context.worker
    event = {"accountNumber": account_number, "amount": amount}
    worker.consumer.produce(event)


@when(u'I withdrawn from the account with "{amount}" credit')
def step_impl(context, amount):
    account_number = context.account_number
    worker = context.worker
    event = {"accountNumber": account_number, "amount": amount}
    worker.consumer.produce(event)


@then(u'the account should has "{final_balance:d}" credit(s)')
def step_impl(context, final_balance):
    account_number = context.account_number
    balance_repository = context.balance_repository
    assert balance_repository.fetch_by_account_number(
        account_number)['clearedBalance'] == final_balance
