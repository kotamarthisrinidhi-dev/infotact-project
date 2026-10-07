import json
import time
import pandas as pd
try:
    from kafka import KafkaProducer
    from kafka.errors import KafkaError  # pyright: ignore[reportMissingModuleSource]
except ImportError as exc:
    raise ImportError(
        "Kafka client is not installed. Install it with: pip install kafka-python"
    ) from exc


# --------------------------------
# Kafka Configuration
# --------------------------------

KAFKA_SERVER = "localhost:9092"
TOPIC_NAME = "atmosync_microclimate"

CSV_FILE = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\data_loading\atmosync_microclimate_raw.csv"


# --------------------------------
# Create Kafka Producer
# --------------------------------

try:

    producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda value:
        json.dumps(value).encode("utf-8"),
    key_serializer=lambda key:
        key.encode("utf-8"),
    acks="all",
    retries=3,
    batch_size=16384,
    linger_ms=10
)

    print("Connected to Kafka successfully.")

except Exception as error:

    print(f"Kafka connection failed: {error}")
    exit()


# --------------------------------
# Read Dataset
# --------------------------------

try:

    df = pd.read_csv(CSV_FILE)

    print(f"Loaded {len(df)} records.")

except Exception as error:

    print(f"Dataset loading failed: {error}")
    producer.close()
    exit()


# --------------------------------
# Send Records
# --------------------------------

successful_records = 0
failed_records = 0


for _, row in df.iterrows():

    message = {
        "date": str(row["date"]),
        "location": row["location"],
        "latitude": row["latitude"],
        "longitude": row["longitude"],
        "elevation_m": row["elevation_m"],
        "area_profile": row["area_profile"],
        "temp_max_c": row["temp_max_c"],
        "temp_min_c": row["temp_min_c"],
        "rainfall_mm": row["rainfall_mm"],
        "humidity_pct": row["humidity_pct"],
        "wind_speed_kmph": row["wind_speed_kmph"]
    }

    try:

        future = producer.send(
    TOPIC_NAME,
    key=str(message["location"]),
    value=message
    )
        # Wait for Kafka acknowledgement
        future.get(timeout=10)

        successful_records += 1

        print(
            f"Sent record {successful_records}: "
            f"{message['location']}"
        )

    except KafkaError as error:

        failed_records += 1

        print(
            f"Failed to send record: {error}"
        )

    time.sleep(0.05)


# --------------------------------
# Finish
# --------------------------------

producer.flush()
producer.close()


# --------------------------------
# Summary
# --------------------------------

print("\n==============================")
print("Kafka Producer Summary")
print("==============================")

print(f"Successful records : {successful_records}")
print(f"Failed records     : {failed_records}")
print(f"Total records      : {len(df)}")

if failed_records == 0:
    print("\nKafka ingestion completed successfully.")
else:
    print("\nKafka ingestion completed with errors.")