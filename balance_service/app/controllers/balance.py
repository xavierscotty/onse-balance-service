from flask import Blueprint, jsonify, current_app
from http import HTTPStatus


from balance_service.app.infrastructure.balance_repository import AccountNotFound

balance = Blueprint('balance', __name__, url_prefix='/balance')


@balance.route('/<string:accountNumber>', methods=['GET'])
def get_balance(accountNumber):
    repository = current_app.extensions['redis']
    result = repository.fetch_by_account_number(accountNumber)
    if result == None:
        raise AccountNotFound()
    return jsonify(result), HTTPStatus.OK


@balance.errorhandler(AccountNotFound)
def handle_bad_request(e):
    return jsonify({
        'message': e.message
    }), HTTPStatus.NOT_FOUND
