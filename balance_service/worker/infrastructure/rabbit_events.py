from pika import ConnectionParameters, BlockingConnection

from balance_service.worker.utils import transpose_event


class RabbitConnection:
    def __init__(self, config):
        params = ConnectionParameters(host=config.RABBITMQ_HOST,
                                      heartbeat_interval=int(
                                          config.RABBITMQ_HEARTBEAT_INTERVAL),
                                      blocked_connection_timeout=int(config.RABBITMQ_HEARTBEAT_INTERVAL))
        self._connection = BlockingConnection(params)

    def get_channel(self):
        return self._connection.channel()


class RabbitConsumer(RabbitConnection):
    def __init__(self, config):
        super().__init__(config)
        self.queue = config.RABBITMQ_CONSUMER_QUEUE
        # ----------------- to remove ---------------
        channel = self.get_channel()
        channel.queue_declare(queue=self.queue)
        channel.close()

    def on_event(self, action):
        def callback(ch, method, properties, body):
            payload = transpose_event(body)
            action(payload)
        channel = self.get_channel()
        channel.basic_consume(queue=self.queue,
                              consumer_callback=callback,
                              no_ack=True)
        channel.start_consuming()
