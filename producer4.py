from kafka import KafkaProducer, producer
import json
from roman_class import Roman
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')
producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], value_serializer = json_serializer)

if __name__ == "__main__":
    obj = Roman()
    for i in ['IX', 'D', 'CXX', 'LIX', 'VII', 'XIXX', 'XCIX']:
        Integer_val = obj.roman_to_int(i)
        print(Integer_val)
        producer.send("Roman_to_Integer", Integer_val)
        time.sleep(2)