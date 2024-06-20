#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost"),
)
channel = connection.channel()
channel.queue_declare(queue="task_queue", durable=True)
i = 0

while True:
    i += 1
    message = "Message " + str(i)
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent,
        ),
    )
    print(f" [x] Sent {message}")
    time.sleep(3)

connection.close()
