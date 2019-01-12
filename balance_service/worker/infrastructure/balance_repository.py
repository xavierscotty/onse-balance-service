from json import loads, dumps

from redis import Redis


class RedisJsonConnection:
    def __init__(self, config):
        self.config = config
        self._connection = Redis.from_url(self.config.REDIS_URL)

    def _set(self, key, value):
        self._connection.set(key, dumps(value))

    def _get(self, key):
        result = self._connection.get(key)
        if result is None:
            return None
        return loads(result)


class BalanceRepository(RedisJsonConnection):
    def __init__(self, config):
        super().__init__(config)

    def store(self, account_number, account_data):
        self._set(
            f'{self.config.BALANCE_NAMESPACE}:{account_number}', account_data)

    def fetch_by_account_number(self, account_number):
        result = self._get(f'{self.config.BALANCE_NAMESPACE}:{account_number}')
        if result is None:
            return None
        return result
