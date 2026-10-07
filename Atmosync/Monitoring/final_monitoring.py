import socket

KAFKA_HOST = "localhost"
KAFKA_PORT = 9092


def test_kafka():

    try:
        connection = socket.create_connection(
            (KAFKA_HOST, KAFKA_PORT),
            timeout=3
        )

        connection.close()
        return True

    except Exception:
        return False


def main():

    print("=" * 50)
    print("AtmoSync Final Monitoring Test")
    print("=" * 50)

    kafka_status = test_kafka()

    print(
        f"Kafka Broker: "
        f"{'AVAILABLE' if kafka_status else 'UNAVAILABLE'}"
    )

    if kafka_status:
        print("\nFINAL MONITORING TEST: PASSED")
        print("Critical service is available.")
    else:
        print("\nFINAL MONITORING TEST: FAILED")
        print("Kafka broker is unavailable.")


if __name__ == "__main__":
    main()