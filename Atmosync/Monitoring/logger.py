import logging
import os
from datetime import datetime


# Create logs directory
os.makedirs("logs", exist_ok=True)


# Log file
log_file = "logs/atmosync_pipeline.log"


# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_pipeline_start():
    logging.info("AtmoSync pipeline started")
    print("Pipeline started")


def log_records_processed(count):
    logging.info(f"Records processed: {count}")
    print(f"Records processed: {count}")


def log_kafka_status(status):
    logging.info(f"Kafka status: {status}")
    print(f"Kafka status: {status}")


def log_snowflake_status(status):
    logging.info(f"Snowflake status: {status}")
    print(f"Snowflake status: {status}")


def log_validation_status(status):
    logging.info(f"Validation status: {status}")
    print(f"Validation status: {status}")


def log_pipeline_end():
    logging.info("AtmoSync pipeline completed")
    print("Pipeline completed")


def log_error(error):
    logging.error(f"Pipeline error: {error}")
    print(f"ERROR: {error}")


if __name__ == "__main__":

    log_pipeline_start()

    log_records_processed(0)

    log_kafka_status("Configured")

    log_snowflake_status("Configured")

    log_validation_status("Pending")

    log_pipeline_end()

    print(f"\nLog file created: {log_file}")