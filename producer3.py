from kafka import KafkaProducer, producer
import json
from assignment1 import dictionary_movie_data
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')
producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], value_serializer = json_serializer)

if __name__ == "__main__":
    while True:
        movies_synopsis = dictionary_movie_data
        print(movies_synopsis)
        producer.send("top_movies_synopsis", movies_synopsis)
        time.sleep(2)