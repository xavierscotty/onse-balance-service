# -*- coding: utf-8 -*-
"""Application configuration."""
from os import environ


class config(object):
    """Base configuration."""
    ### APPLICATION ###
    APP_NAME = environ.get('APP_NAME') or 'Balance Service Worker'
    ### Redis ###
    REDIS_URL = environ.get('REDIS_URL') or 'redis://localhost:6379/0'
    BALANCE_NAMESPACE = environ.get('BALANCE_NAMESPACE') or 'balance'
    ENV = environ.get('ENV') or 'development'
    ### RabbitMQ ###
    RABBITMQ_HOST = environ.get('RABBITMQ_HOST') or ''
    RABBITMQ_CONSUMER_QUEUE = environ.get('RABBITMQ_CONSUMER_QUEUE') or ''
    RABBITMQ_HEARTBEAT_INTERVAL = environ.get(
        'RABBITMQ_HEARTBEAT_INTERVAL') or 600
    RABBITMQ_CONNECTION_TIMEOUT = environ.get(
        'RABBITMQ_CONNECTION_TIMEOUT') or 300


class test_config():
    """Testing configuration."""
    TESTING = 'true'
    ENV = 'testing'

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN DEBUG MODE. \
                YOU SHOULD NOT SEE THIS IN PRODUCTION.')
