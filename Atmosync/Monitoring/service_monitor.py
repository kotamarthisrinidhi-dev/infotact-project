import socket

KAFKA_HOST = "localhost"
KAFKA_PORT = 9092


def check_kafka():
    try:
        connection = socket.create_connection(
            (KAFKA_HOST, KAFKA_PORT),
            timeout=3
        )
        connection.close()
        return True
    except Exception:
        return False


def check_service(name, status):
    if status:
        print(f"{name}: AVAILABLE")
    else:
        print(f"{name}: UNAVAILABLE")


def main():

    print("==============================")
    print("AtmoSync Service Monitor")
    print("==============================")

    kafka_status = check_kafka()

    check_service("Kafka Broker", kafka_status)

    if kafka_status:
        print("\nOverall Status: HEALTHY")
    else:
        print("\nOverall Status: ATTENTION REQUIRED")


if __name__ == "__main__":
    main()