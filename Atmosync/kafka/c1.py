import json
import math
from kafka import KafkaConsumer
import snowflake.connector

# -----------------------------
# Kafka Configuration
# -----------------------------
KAFKA_SERVER = "localhost:9092"
TOPIC_NAME = "atmosync_microclimate"
GROUP_ID = "atmosync-snowflake-consumer"

# -----------------------------
# Snowflake Configuration
# -----------------------------
SNOWFLAKE_ACCOUNT = "YOUR_ACCOUNT"
SNOWFLAKE_USER = "YOUR_USERNAME"
SNOWFLAKE_PASSWORD = "YOUR_PASSWORD"
SNOWFLAKE_WAREHOUSE = "YOUR_WAREHOUSE"

# -----------------------------
# Connect to Snowflake
# -----------------------------
conn = snowflake.connector.connect(
    account="GZGDCQH-UU35933",
    user="ROHITHAREDDY",
    password="Rabbitreddy@2005",
    warehouse="COMPUTE_WH",
    database="ATMOSYNC_DB",
    schema="STAGING"
)

cursor = conn.cursor()

print("Connected to Snowflake successfully.")

# -----------------------------
# Kafka Consumer
# -----------------------------
consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_SERVER,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id=GROUP_ID,
    value_deserializer=lambda value:
        json.loads(value.decode("utf-8"))
)

print("Kafka consumer started.")
print(f"Listening to: {TOPIC_NAME}")

count = 0

try:

    for message in consumer:

        data = message.value

        sql = """
INSERT INTO ATMOSYNC_DB.STAGING.KAFKA_MICROCLIMATE_STAGING
(
    DATE,
    LOCATION,
    LATITUDE,
    LONGITUDE,
    ELEVATION_M,
    AREA_PROFILE,
    TEMP_MAX_C,
    TEMP_MIN_C,
    RAINFALL_MM,
    HUMIDITY_PCT,
    WIND_SPEED_KMPH,
    KAFKA_PARTITION,
    KAFKA_OFFSET
)
VALUES (
    %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s
)
"""

        values = (
            data.get("date"),
            data.get("location"),
            data.get("latitude"),
            data.get("longitude"),
            data.get("elevation_m"),
            data.get("area_profile"),
            data.get("temp_max_c"),
            data.get("temp_min_c"),
            data.get("rainfall_mm"),
            data.get("humidity_pct"),
            data.get("wind_speed_kmph"),
            message.partition,
            message.offset
        )

        values = tuple(
            None if isinstance(v, float) and math.isnan(v) else v
            for v in values
        )

        cursor.execute(sql, values)
        conn.commit()

        count += 1

        print(
            f"Inserted record {count} | "
            f"Location: {data['location']} | "
            f"Partition: {message.partition} | "
            f"Offset: {message.offset}"
        )

except KeyboardInterrupt:

    print("\nConsumer stopped by user.")

finally:

    cursor.close()
    conn.close()
    consumer.close()

    print(f"\nTotal records inserted: {count}")