import json
from kafka import KafkaConsumer

KAFKA_SERVER = "localhost:9092"
TOPIC_NAME = "atmosync_microclimate"


def test_kafka_messages():

    print("=" * 50)
    print("AtmoSync Kafka Producer Test")
    print("=" * 50)

    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=KAFKA_SERVER,
        auto_offset_reset="earliest",
        enable_auto_commit=False,
        group_id="atmosync-producer-test",
        value_deserializer=lambda value:
            json.loads(value.decode("utf-8")),
        consumer_timeout_ms=5000
    )

    count = 0

    for record in consumer:

        count += 1

        if count <= 5:
            print(
                f"Record {count}: "
                f"location={record.value.get('location')}, "
                f"partition={record.partition}, "
                f"offset={record.offset}"
            )

    consumer.close()

    print("-" * 50)
    print(f"Kafka records detected: {count}")

    if count > 0:
        print("PRODUCER TEST PASSED")
    else:
        print("PRODUCER TEST FAILED")


if __name__ == "__main__":
    test_kafka_messages()