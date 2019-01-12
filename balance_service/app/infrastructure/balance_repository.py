from json import loads, dumps

from flask_redis import FlaskRedis

from balance_service.worker.config import config


class RedisJsonFlaskConnection(FlaskRedis):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _set(self, key, value):
        self.set(key, dumps(value))

    def _get(self, key):
        result = self.get(key)
        if result is None:
            return None
        return loads(result)


class BalanceRepository(RedisJsonFlaskConnection):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def store(self, account_number, account_data):
        self._set(f'{config.BALANCE_NAMESPACE}:{account_number}', account_data)

    def fetch_by_account_number(self, account_number):
        return self._get(f'{config.BALANCE_NAMESPACE}:{account_number}')


class AccountNotFound(RuntimeError):
    def __init__(self, message='Account not found'):
        self.message = message
