import json
import time
import requests
from kafka import KafkaProducer
from dotenv import load_dotenv

# Stock API Configuration from Alpha Vantage
load_dotenv()
API_Key = os.getenv("API_KEY")