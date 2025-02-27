import os
import json
import time
import requests
from kafka import KafkaProducer
from dotenv import load_dotenv

# Stock API Configuration from Alpha Vantage
load_dotenv()
API_KEY = os.getenv("API_KEY")

STOCK_SYMBOL = "AAPL"
KAFKA_TOPIC = "stock_prices"
KAFKA_BROKER = "localhost:9092"

# Kafka Producer Configuration
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def fetch_stock_price():
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK_SYMBOL}&interval=1min&apikey={API_KEY}"
    response = requests.get(url).json()

    try:
        latest_time = list(response["Time Series (1min)"].keys())[0]
        stock_data = {
            "symbol": STOCK_SYMBOL,
            "timestamp": latest_time,
            "open":float(response["Time Series (1min)"][latest_time]["1. open"]),
            "high":float(response["Time Series (1min)"][latest_time]["2. high"]),
            "low":float(response["Time Series (1min)"][latest_time]["3. low"]),
            "close":float(response["Time Series (1min)"][latest_time]["4. close"]),
            "volume":float(response["Time Series (1min)"][latest_time]["5. volume"]),
        }
        return stock_data
    except KeyError:
        return None
    
while True:
    stock_data = fetch_stock_price()
    if stock_data:
        print(f"Sending data to Kafka: {stock_data}")
        producer.send(KAFKA_TOPIC, stock_data)
        time.sleep(60) # Fetch stock data every minute