from flask_redis import FlaskRedis


class BalanceRepository(FlaskRedis):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def store(self, account_number, account_data):
        self.set(account_number, account_data)

    def fetch_by_account_number(self, account_number):
        result = self.get(f'balance:{account_number}')
        if result == None:
            raise AccountNotFound()
        return result


class AccountNotFound(RuntimeError):
    def __init__(self, message='Account not found'):
        self.message = message
