from kafka import KafkaConsumer, consumer
import json

if __name__=="__main__":
    consumer = KafkaConsumer(
        "Bank_Transactions",
        bootstrap_servers='127.0.0.1:9092',
        auto_offset_reset='earliest',
        group_id='consumer_group-c'
    )

    for item in consumer:
        print(json.loads(item.value))