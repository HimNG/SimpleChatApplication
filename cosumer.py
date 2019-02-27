import pika

credentials = pika.PlainCredentials('guqfdihk', 'l4TRIgRf5e3Va6qrQCnMoKrcN5LNuZtE',erase_on_connect=False)
connection = pika.BlockingConnection(pika.ConnectionParameters('dinosaur.rmq.cloudamqp.com',1883, '/',credentials))
channel = connection.channel()


channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()