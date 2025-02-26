#!/usr/bin/env python
# coding=utf-8
import pika


credentials = pika.PlainCredentials('user_test', '24101967cO')
parameters = pika.ConnectionParameters('mq1', '5672', '/', credentials)
connection = pika.BlockingConnection(parameters)
#connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.7'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello Netology!')
connection.close()
