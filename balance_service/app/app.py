from flask import Flask

from balance_service.app.controllers.swagger import setup_swagger
from balance_service.app.controllers.heatlh import health
from balance_service.app.controllers.balance import balance


def create(config, repository):
    app = Flask(__name__)
    app.config.from_object(config)
    repository.init_app(app)
    register_blueprints(app)

    app.register_blueprint(setup_swagger(), url_prefix=config.SWAGGER_URL)
    return app


def register_blueprints(app):
    """Register blueprints with the Flask application."""
    app.register_blueprint(health)
    app.register_blueprint(balance)
