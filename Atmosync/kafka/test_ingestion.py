from kafka import KafkaConsumer
import json

TOPIC = "atmosync_microclimate"
KAFKA_SERVER = "localhost:9092"


def test_kafka_messages():

    print("=" * 45)
    print("AtmoSync Kafka Ingestion Test")
    print("=" * 45)

    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=KAFKA_SERVER,
        auto_offset_reset="earliest",
        enable_auto_commit=False,
        group_id="atmosync-final-test",
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

    print("-" * 45)
    print(f"Kafka records detected: {count}")

    if count > 0:
        print("END-TO-END KAFKA TEST PASSED")
    else:
        print("END-TO-END KAFKA TEST FAILED")


if __name__ == "__main__":
    test_kafka_messages()