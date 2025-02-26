#!/usr/bin/env python
# coding=utf-8
import pika

credentials = pika.PlainCredentials('user_test', '24101967cO')
parameters = pika.ConnectionParameters('mq1', '5672', '/', credentials)
connection = pika.BlockingConnection(parameters)
#connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume('hello', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
