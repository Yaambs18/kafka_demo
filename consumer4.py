from kafka import KafkaConsumer, consumer
import json

if __name__=="__main__":
    consumer = KafkaConsumer(
        "Roman_to_Integer",
        bootstrap_servers='127.0.0.1:9092',
        auto_offset_reset='earliest',
        group_id='consumer_group-d'
    )

    for item in consumer:
        num = json.loads(item.value)
        if num > 50:
            print(num)