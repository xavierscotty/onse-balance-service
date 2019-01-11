from balance_service.worker.config import config, test_config


def test_default_config():
    assert hasattr(config, 'RABBITMQ_HOST')
    assert hasattr(config, 'RABBITMQ_CONSUMER_QUEUE')
    assert hasattr(config, 'RABBITMQ_HEARTBEAT_INTERVAL')
    assert hasattr(config, 'RABBITMQ_CONNECTION_TIMEOUT')
    assert hasattr(config, 'ENV')
    assert hasattr(config, 'REDIS_URL')
    assert hasattr(config, 'BALANCE_NAMESPACE')


def test_test_config():
    assert hasattr(test_config, 'TESTING')
