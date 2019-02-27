from tkinter import *
import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    
	
root = Tk()
T = Text(root, height=20, width=30)
T.pack()
T.insert(END, "Just a text Widget\nin two lines\n")
mainloop()

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')


channel.basic_consume(callback,queue='hello',no_ack=True)
channel.start_consuming()
   
