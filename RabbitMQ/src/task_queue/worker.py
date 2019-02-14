import time

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#Make sure queue exists or create if it doesn't.
channel.queue_declare(queue='hello')

#Define a callback
def callback(ch, method, properties, body):
    print(" [x] Recieved %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] done")

#Assign callback to queue
channel.basic_consume(callback, queue='hello', no_ack=True)

#Wait on the queue for message
print(" [*] Waiting for messages")
channel.start_consuming()
