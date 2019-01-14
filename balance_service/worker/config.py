# -*- coding: utf-8 -*-
"""Application configuration."""
from os import environ


class config(object):
    """Base configuration."""
    # APPLICATION
    APP_NAME = environ.get('APP_NAME', 'Balance Service Worker')
    # Redis
    REDIS_URL = environ.get('REDIS_URL', 'redis://localhost:6379/0')
    BALANCE_NAMESPACE = environ.get('BALANCE_NAMESPACE', 'balance')
    ENV = environ.get('ENV', 'development')
    # RabbitMQ
    RABBITMQ_HOST = environ.get('RABBITMQ_HOST', '')
    RABBITMQ_CONSUMER_EXCHANGE = environ.get('RABBITMQ_CONSUMER_EXCHANGE', '')
    RABBITMQ_CONSUMER_QUEUE = environ.get('RABBITMQ_CONSUMER_QUEUE', '')
    RABBITMQ_HEARTBEAT_INTERVAL = environ.get('RABBITMQ_HEARTBEAT_INTERVAL',
                                              600)
    RABBITMQ_CONNECTION_TIMEOUT = environ.get('RABBITMQ_CONNECTION_TIMEOUT',
                                              300)


class test_config():
    """Testing configuration."""
    TESTING = 'true'
    ENV = 'testing'

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN DEBUG MODE. \
                YOU SHOULD NOT SEE THIS IN PRODUCTION.')
