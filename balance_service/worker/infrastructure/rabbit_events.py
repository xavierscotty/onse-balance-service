from pika import ConnectionParameters, BlockingConnection

from balance_service.worker.utils import transpose_event


class RabbitConnection:
    def __init__(self, config, logger):
        logger.info('Connecting to RabbitMQ', host=config.RABBITMQ_HOST)

        params = ConnectionParameters(
            host=config.RABBITMQ_HOST,
            heartbeat_interval=int(config.RABBITMQ_HEARTBEAT_INTERVAL),
            blocked_connection_timeout=int(config.RABBITMQ_HEARTBEAT_INTERVAL))

        self._connection = BlockingConnection(params)

        channel = self._get_channel()

        self._exchange = config.RABBITMQ_CONSUMER_EXCHANGE
        channel.exchange_declare(self._exchange, exchange_type='fanout')

    def _get_channel(self):
        return self._connection.channel()


class RabbitConsumer(RabbitConnection):
    def __init__(self, config, logger):
        super().__init__(config, logger)

        self.queue = config.RABBITMQ_CONSUMER_QUEUE

        channel = self._get_channel()
        channel.queue_declare(queue=self.queue)
        channel.queue_bind(queue=self.queue, exchange=self._exchange)

    def on_event(self, action):
        def callback(ch, method, properties, body):
            payload = transpose_event(body)
            action(payload)

        channel = self._get_channel()
        channel.basic_consume(queue=self.queue,
                              consumer_callback=callback,
                              no_ack=True)
        channel.start_consuming()
