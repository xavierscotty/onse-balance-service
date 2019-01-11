from balance_service.app.infrastructure.balance_repository import AccountNotFound


class MockBalanceRepository():
    def __init__(self, config_prefix='REDIS'):
        self.__store = dict()
        self.config_prefix = config_prefix

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions[self.config_prefix.lower()] = self

    def store(self, account_number, account_data):
        self.__store[account_number] = str(account_data)

    def fetch_by_account_number(self, account_number):
        result = self.__store.get(account_number)
        if result == None:
            raise AccountNotFound
        return result
