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
        balance = int(event['balance'])

        data = {
            'accountNumber': account_number,
            'clearedBalance': balance
        }

        self.balance.store(account_number, data)

        self.logger.debug(f'Successfully sync balance:',
                          process_event='update-balance')
