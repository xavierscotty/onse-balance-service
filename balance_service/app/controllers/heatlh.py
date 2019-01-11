from flask import Blueprint, jsonify

health = Blueprint('health', __name__, url_prefix='/balance')


@health.route('/health')
def healthcheck():
    return jsonify(message='OK')
