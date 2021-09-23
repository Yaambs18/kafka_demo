from kafka import KafkaConsumer, consumer
import json


if __name__ == "__main__":
    consumer = KafkaConsumer(
        "ipl_team_data",
        bootstrap_servers='127.0.0.1:9092',
        auto_offset_reset='earliest',
        group_id='consumer_group-b'
    )
    print("consumer started")
    for data in consumer:
        print("IPL teams data: \n {}".format(json.loads(data.value)))