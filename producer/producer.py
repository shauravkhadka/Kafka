import random
import time
from kafka import KafkaProducer
from kafka.errors import KafkaError
from statistics import mean

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    key_serializer=lambda k: k.encode('utf-8'),
    value_serializer=lambda v: str(v).encode('utf-8')
)

keys = [f"key{i}" for i in range(1, 11)]
values = []

def on_send_success(record_metadata):
    global values
    if record_metadata.value is not None:
        values.append(int(record_metadata.value.decode('utf-8')))
    if len(values) == 10000:
        print(f"Average of produced values: {mean(values)}")
        values.clear()

def on_send_error(excp):
    print(f"I am an errback {str(excp)}")

while True:
    key = random.choice(keys)
    value = random.randint(0, 100)
    producer.send('test2', key=key, value=value).add_callback(on_send_success).add_errback(on_send_error)
    time.sleep(0.001)
