from kafka import KafkaProducer, producer
import json
from web_scraping_book import tw_star_rating
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')
producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], value_serializer = json_serializer)

if __name__ == "__main__":
    while True:
        books_list = tw_star_rating
        print(books_list)
        producer.send("two_star_rating_books", books_list)
        time.sleep(2)