from flask import current_app, Blueprint, jsonify

health = Blueprint('health', __name__, url_prefix='/')


@health.route('/health')
def healthcheck():
    return jsonify(message='OK')
