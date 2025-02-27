import os
import requests
from dotenv import load_dotenv

# Fetch API key
load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("10 API_KEY not found")
# Get Apple price
STOCK_SYMBOL = "AAPL"

# Alpha Vantage API URL
# url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK_SYMBOL}&interval=1min&apikey={API_KEY}"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_SYMBOL}&apikey={API_KEY}"
def fetch_stock_price():
    response = requests.get(url).json()

    try:
        # Get the most recent timestamp
        latest_time = list(response["Time Series (1min)"].keys())[0]
        stock_data = response["Time Series (1min)"][latest_time]

        # Print stock details
        print(f"Stock Data for {STOCK_SYMBOL} at {latest_time}")
        print(f"Open: {stock_data['1. open']}")
        print(f"High: {stock_data['2. high']}")
        print(f"Low: {stock_data['3. low']}")
        print(f"Close: {stock_data['4. close']}")
        print(f"Volume: {stock_data['5. volume']}")

    except KeyError:
        print("Error fetching stock data")

# Run test
fetch_stock_price()