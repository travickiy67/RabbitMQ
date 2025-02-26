#!/usr/bin/env python
# coding=utf-8
import pika

credentials = pika.PlainCredentials('test_user', '24101967cO')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.8', 5672, 'test_host', credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.queue_declare(queue='test')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

    channel.basic_qos(prefetch_count=1)
channel.basic_consume('hello', on_message_callback=callback, auto_ack=False)
channel.basic_consume('test', on_message_callback=callback, auto_ack=True)
#channel.basic_consume(callback, queue='hello', no_ack=True)

channel.start_consuming()
