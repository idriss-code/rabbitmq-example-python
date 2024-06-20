#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

i = 0

while True:
    i += 1
    message = "Message " + str(i)
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message)

    print(" [x] Sent "+message)

    time.sleep(3)

connection.close()
