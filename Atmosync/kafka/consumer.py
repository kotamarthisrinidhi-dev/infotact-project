import json
from kafka import KafkaConsumer

KAFKA_SERVER = "localhost:9092"
TOPIC_NAME = "atmosync_microclimate"

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_SERVER,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="atmosync-snowflake-consumer",
    value_deserializer=lambda value: json.loads(
        value.decode("utf-8")
    )
)

print("AtmoSync Kafka Consumer Started")
print(f"Topic: {TOPIC_NAME}")

count = 0

try:
    for message in consumer:

        data = message.value
        count += 1

        print("\nReceived record:")
        print(data)

        print(f"Partition: {message.partition}")
        print(f"Offset: {message.offset}")

        if count >= 10:
            break

finally:
    consumer.close()
    print(f"\nConsumer stopped.")
    print(f"Records received: {count}")