import sys

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#Create a queue
channel.queue_declare(queue='hello')

#Create task message from input
message = ' '.join(sys.argv[1:]) or "Hello World!"

#send message
channel.basic_publish(exchange='', routing_key='hello', body=message)

print(" [x] Sent 'Hello World!'")

#flush buffers and close connection
connection.close()
