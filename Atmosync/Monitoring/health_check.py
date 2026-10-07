import os
from datetime import datetime


def check_dataset():
    """Check whether the AtmoSync dataset exists."""

    file_path = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\data_loading\atmosync_microclimate_raw.csv"

    if os.path.exists(file_path):
        return True, "Dataset available"

    return False, "Dataset not found"


def check_kafka():
    """
    Basic Kafka configuration check.
    Actual connectivity is verified by the Kafka producer.
    """

    kafka_server = "localhost:9092"

    if kafka_server:
        return True, f"Kafka configured at {kafka_server}"

    return False, "Kafka configuration missing"


def check_snowflake():
    """
    Basic Snowflake configuration check.
    """

    database = "ATMOSYNC_DB"
    schema = "RAW"

    if database and schema:
        return True, f"Snowflake configured: {database}.{schema}"

    return False, "Snowflake configuration missing"


def generate_health_report():
    """Generate AtmoSync pipeline health report."""

    print("=" * 50)
    print("       AtmoSync Pipeline Health Check")
    print("=" * 50)

    print(f"Time: {datetime.now()}")

    checks = [
        ("Dataset", check_dataset()),
        ("Kafka", check_kafka()),
        ("Snowflake", check_snowflake())
    ]

    all_healthy = True

    for service, result in checks:

        status, message = result

        if status:
            print(f"[OK]   {service}: {message}")
        else:
            print(f"[FAIL] {service}: {message}")
            all_healthy = False

    print("=" * 50)

    if all_healthy:
        print("Overall Status: HEALTHY")
    else:
        print("Overall Status: ATTENTION REQUIRED")

    print("=" * 50)


if __name__ == "__main__":
    generate_health_report()