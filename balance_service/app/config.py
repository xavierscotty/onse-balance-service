# -*- coding: utf-8 -*-
"""Application configuration."""
from os import environ


class config(object):
    """Base configuration."""
    # SWAGGER
    SWAGGER_URL = environ.get('SWAGGER_URL') or '/docs'
    SWAGGER_FILE_PATH = environ.get(
        'SWAGGER_FILE_PATH') or '/../../../swagger.yml'
    # APPLICATION
    APP_NAME = environ.get('APP_NAME') or 'Balance Service App'
    PORT = environ.get('PORT') or '5000'
    # Redis
    REDIS_URL = environ.get('REDIS_URL') or 'redis://localhost:6379/0'
    BALANCE_NAMESPACE = environ.get('BALANCE_NAMESPACE') or 'balance'
    ENV = environ.get('ENV') or 'development'


class test_config():
    """Testing configuration."""
    TESTING = 'true'
    ENV = 'testing'
    # SWAGGER
    SWAGGER_URL = environ.get('SWAGGER_URL') or '/docs'
    SWAGGER_FILE_PATH = environ.get(
        'SWAGGER_FILE_PATH') or '/../../../swagger.yml'

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN DEBUG MODE. \
                YOU SHOULD NOT SEE THIS IN PRODUCTION.')
