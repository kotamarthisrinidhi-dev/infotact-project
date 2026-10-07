import socket
import snowflake.connector

KAFKA_HOST = "localhost"
KAFKA_PORT = 9092

SNOWFLAKE_ACCOUNT = "YOUR_ACCOUNT"
SNOWFLAKE_USER = "YOUR_USERNAME"
SNOWFLAKE_PASSWORD = "YOUR_PASSWORD"
SNOWFLAKE_WAREHOUSE = "YOUR_WAREHOUSE"


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


def check_snowflake():
    try:
        conn = snowflake.connector.connect(
            account=SNOWFLAKE_ACCOUNT,
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            warehouse=SNOWFLAKE_WAREHOUSE
        )

        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()

        cursor.close()
        conn.close()

        return True

    except Exception:
        return False


def main():

    print("=" * 40)
    print("AtmoSync Pipeline Monitor")
    print("=" * 40)

    kafka_status = check_kafka()
    snowflake_status = check_snowflake()

    print(
        f"Kafka Broker: "
        f"{'AVAILABLE' if kafka_status else 'UNAVAILABLE'}"
    )

    print(
        f"Snowflake: "
        f"{'AVAILABLE' if snowflake_status else 'UNAVAILABLE'}"
    )

    if kafka_status and snowflake_status:
        print("\nOverall Status: HEALTHY")
    else:
        print("\nOverall Status: ATTENTION REQUIRED")


if __name__ == "__main__":
    main()