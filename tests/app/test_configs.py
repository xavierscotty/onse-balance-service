from flask import Flask

from balance_service.app import config

def test_development_config():
    app = Flask(__name__)
    app.config.from_object(config.dev_config)
    assert app.config['ENV'] == 'development'
    assert not app.config['TESTING']


def test_default_config():
    app = Flask(__name__)
    app.config.from_object(config.config)
    assert app.config['SWAGGER_URL']
    assert app.config['SWAGGER_FILE_PATH']
    assert app.config['APP_NAME']
    assert app.config['REDIS_URL']
    assert app.config['ENV'] == 'production'


def test_test_config():
    app = Flask(__name__)
    app.config.from_object(config.test_config)
    assert app.config['TESTING']
    assert app.config['TESTING'] == 'true'
