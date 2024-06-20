#!/usr/bin/env python
import pika


def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")


connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5673))
channel = connection.channel()

channel.queue_declare(queue='corrum', durable=True,
                      arguments={'x-queue-type': 'quorum'})

channel.basic_consume(queue='corrum',
                      auto_ack=True,
                      on_message_callback=callback)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
