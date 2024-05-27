from kafka import KafkaConsumer
from statistics import mean

consumer = KafkaConsumer(
    'test2',
    bootstrap_servers=['localhost:9092'],
    group_id='group1',
    key_deserializer=lambda k: k.decode('utf-8'),
    value_deserializer=lambda v: int(v.decode('utf-8')),
    auto_offset_reset='earliest'
)

values = []

for message in consumer:
    values.append(message.value)
    if len(values) == 10000:
        print(f"Average of consumed values: {mean(values)}")
        values.clear()
