#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

exchangeName = 'fanoutex'

result = channel.exchange_declare(exchange=exchangeName,exchange_type='fanout')

i = 0

while True:
    i += 1
    message = "Message " + str(i)
    channel.basic_publish(exchange=exchangeName,
                          routing_key='',
                          body=message)
    print(" [x] Sent "+message)

    time.sleep(3)

connection.close()
