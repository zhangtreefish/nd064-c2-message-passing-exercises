import json

from kafka import KafkaProducer
from flask import Flask, jsonify, request, g, Response

import services

app = Flask(__name__)

@app.before_request
def before_request():
    # Set up a Kafka producer
    TOPIC_NAME = 'items'
    KAFKA_SERVER = 'localhost:9092'
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
    # Setting Kafka to g enables us to use this
    # in other parts of our application
    g.kafka_producer = producer

"""
@oas [get] /health
description: "Helath check endpoint"
"""
@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})


@app.route('/api/orders/computers', methods=['GET', 'POST'])
def computers():
    if request.method == 'GET':
        return jsonify(services.retrieve_orders())
    elif request.method == 'POST':
        request_body = request.json
        result = services.create_order(request_body)
        return Response(status=202)
    else:
        raise Exception('Unsupported HTTP request type.')


if __name__ == '__main__':
    app.run()
