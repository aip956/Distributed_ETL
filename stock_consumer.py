from kafka import KafkaConsumer
import json

# Kafka Consumer Configuration
KAFKA_TOPIC = "stock_prices"
KAFKA_BROKER = "localhost:9092"

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers = KAFKA_BROKER,
    value_deserializer = lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset = "earliest", # Start from the beginning of topic
    enable_auto_commit = True # Auto mark messages as read
)

# Consume messages
print("Consumer is ready. Waiting for messages . . .")
for message in consumer:
    stock_data = message.value
    print(f"Received stock data: {stock_data}")