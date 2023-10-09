import pprint
import time

import pika
from pika.exceptions import StreamLostError

from settings import RABBIT_HOST


class RabbitMQService:

    def __init__(self, host=RABBIT_HOST, user='user', password='password'):
        self.host = host
        self.user = user
        self.password = password
        self._initialize_connection()

    def _initialize_connection(self):
        """Set up a new connection to RabbitMQ."""
        # Close the existing connection if it's open
        if hasattr(self, "connection") and self.connection.is_open:
            self.connection.close()

        credentials = pika.PlainCredentials(self.user, self.password)
        parameters = pika.ConnectionParameters(host=self.host, credentials=credentials)
        pprint.pprint(credentials)
        pprint.pprint(parameters)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

    def consume_with_retry(self, queue_name, callback, max_retries=5, retry_delay=5):
        """Consume messages with built-in retry logic in case of a StreamLostError."""
        retry_count = 0
        while retry_count < max_retries:
            try:
                self.consume(queue_name, callback)
                # If consumption is successful, break out of the loop
                break
            except StreamLostError:
                print("StreamLostError encountered. Retrying...")
                retry_count += 1
                self._initialize_connection()  # Re-initialize the connection here
                time.sleep(retry_delay)
        if retry_count == max_retries:
            print("Max retries reached. Exiting.")

    def consume(self, queue_name, callback):
        self.channel.queue_declare(queue=queue_name, durable=True)
        self.channel.basic_consume(queue=queue_name,
                                   on_message_callback=callback,
                                   auto_ack=True)
        self.channel.start_consuming()

    def publish(self, queue_name, message):
        self.channel.queue_declare(queue=queue_name, durable=True)
        self.channel.basic_publish(exchange='',
                                   routing_key=queue_name,
                                   body=message,
                                   properties=pika.BasicProperties(delivery_mode=2))  # make message persistent

    def close(self):
        self.connection.close()


def process_message(ch, method, properties, body):
    """Callback function to process incoming messages."""
    print(f"Received: {body.decode()}")
    # Send the received message to the output_queue
    rabbit_service.publish('output_queue', body.decode())
    print(f"Sent to output_queue: {body.decode()}")


if __name__ == '__main__':
    rabbit_service = RabbitMQService()

    try:
        rabbit_service.consume('input_queue', process_message)
    except KeyboardInterrupt:
        print("Stopping service...")
    finally:
        rabbit_service.close()
