from kafka import KafkaProducer, producer
import json
from ipl_scrapper import ipl_data
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')
producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], value_serializer = json_serializer)

if __name__ == "__main__":
    while True:
        ipl_teams = ipl_data()
        print(ipl_teams)
        producer.send("ipl_team_data", ipl_teams)
        time.sleep(2)