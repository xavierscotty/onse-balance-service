from balance_service.app import app
from balance_service.app.config import config
from balance_service.app.infrastructure.balance_repository import \
    BalanceRepository

if __name__ == "__main__":
    balance_repository = BalanceRepository()
    app.create(config=config, repository=balance_repository).run(
        host='0.0.0.0', port=int(config.PORT))
