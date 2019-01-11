from balance_service.worker.model.balance_calculator import BalanceCalculator


class Worker:
    def __init__(self, consumer, balance, logger, config=None):
        self.consumer = consumer
        self.balance = balance
        self.config = config
        self.logger = logger

    def start(self):
        self.logger.info(
            f'Worker -{self.config.APP_NAME}- starts event processing')
        self.consumer.on_event(self.handle_event)

    def handle_event(self, event):
        self.logger.debug('Received balance event:', received_event=event)

        account_number = event['accountNumber']
        amount = int(event['amount'])

        available_balance = self.balance.fetch_by_account_number(
            account_number)
        data = {
            'accountNumber': account_number,
            'clearedBalance': None
        }
        if available_balance == None:
            data['clearedBalance'] = amount
        else:
            self.logger.debug('Found account with balance')
            balance_calculator = BalanceCalculator(
                available_balance['clearedBalance'])
            data['clearedBalance'] = balance_calculator.calculate(amount)

        self.balance.store(account_number, data)

        self.logger.debug(f'Successfulty sync balance:',
                          process_event='update-balance')
