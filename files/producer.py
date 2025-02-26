#!/usr/bin/env python
# coding=utf-8
import pika


credentials = pika.PlainCredentials('test_user', '24101967cO')
parameters = pika.ConnectionParameters('192.168.0.8', '5672', 'test_host', credentials)
connection = pika.BlockingConnection(parameters)
#connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.7'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.queue_declare(queue='test')
channel.basic_publish(exchange='', routing_key='hello', body='Hello Netology!')
channel.basic_publish(exchange='', routing_key='test', body='changing the queue is not difficult')
connection.close()
