from tkinter import *
import pika


def send_message():
   message=e1.get()
   connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
   channel = connection.channel()
   channel.queue_declare(queue='hello')
   channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
   connection.close()
   				  
   print(message) 

def quit_message():
   master.quit()
   

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
	
master = Tk()

e1 = Entry(master)
e1.grid(row=0, column=0)

b1=Button(master, text='Send', command=send_message)
b1.grid(row=0, column=1)

b2=Button(master, text='Quit', command=quit_message)
b2.grid(row=0, column=2) 


mainloop()