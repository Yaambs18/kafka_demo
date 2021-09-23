from kafka import KafkaProducer, producer
import json
from bank_class import Transactions
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')
producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], value_serializer = json_serializer)

if __name__ == "__main__":
    while True:
        Acc_statement = Transactions
        print(Acc_statement)
        producer.send("Bank_Transactions", Acc_statement)
        time.sleep(2)