#!/usr/bin/env python
import pika


def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='fanoutex',
                   queue=queue_name)

channel.basic_consume(queue=queue_name,
                      auto_ack=True,
                      on_message_callback=callback)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
