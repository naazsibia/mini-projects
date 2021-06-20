import pika
import uuid

def on_response(ch, method, props, body):
    print("got a response")
    print(props)
    global response 
    response = body

response = None
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
result = channel.queue_declare(queue='hello')
callback_queue = result.method.queue
channel.basic_consume(queue = callback_queue, on_message_callback=on_response, auto_ack=True)
#channel.basic_publish(exchange='',
 #                     routing_key='hello',
  #                    body='Hello World!')
corr_id = str(uuid.uuid4())
channel.basic_publish(
            exchange='',
            routing_key='hello',
            properties=pika.BasicProperties(
                reply_to=callback_queue,
                correlation_id=corr_id,
            ),
            body="hello")
print(" [x] Sent 'Hello World!'")
connection.process_data_events()
while response is None:
        connection.process_data_events()
print(response)

connection.close()