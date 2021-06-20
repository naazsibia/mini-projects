import pika, sys, os

def on_request(ch, method, props, body):
    print("Message recieved: [x] {}".format(body))
    response = "hey"
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    result = channel.queue_declare(queue='hello')
    callback_queue = result.method.queue
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=callback_queue, on_message_callback=on_request, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)