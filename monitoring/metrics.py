import time
import json
from pathlib import Path
from datetime import datetime


METRICS_FILE = Path("logs/pipeline_metrics.json")


def start_pipeline():
    """Start pipeline timer."""
    return time.time()


def calculate_metrics(start_time, total_records, successful_records, failed_records):
    """Calculate pipeline execution metrics."""

    end_time = time.time()
    execution_time = round(end_time - start_time, 2)

    success_rate = 0

    if total_records > 0:
        success_rate = round(
            (successful_records / total_records) * 100, 2
        )

    metrics = {
        "timestamp": datetime.now().isoformat(),
        "total_records": total_records,
        "successful_records": successful_records,
        "failed_records": failed_records,
        "success_rate_percent": success_rate,
        "execution_time_seconds": execution_time
    }

    return metrics


def save_metrics(metrics):
    """Save pipeline metrics to JSON."""

    METRICS_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(METRICS_FILE, "w") as file:
        json.dump(metrics, file, indent=4)

    print("\nPipeline metrics saved successfully.")
    print(f"Metrics file: {METRICS_FILE}")


def display_metrics(metrics):
    """Display metrics in the terminal."""

    print("\n==============================")
    print("AtmoSync Pipeline Metrics")
    print("==============================")

    print(f"Total records       : {metrics['total_records']}")
    print(f"Successful records  : {metrics['successful_records']}")
    print(f"Failed records      : {metrics['failed_records']}")
    print(f"Success rate        : {metrics['success_rate_percent']}%")
    print(f"Execution time      : {metrics['execution_time_seconds']} seconds")
    print(f"Timestamp           : {metrics['timestamp']}")


if __name__ == "__main__":

    start_time = start_pipeline()

    # Sample metrics for testing
    total_records = 100
    successful_records = 98
    failed_records = 2

    metrics = calculate_metrics(
        start_time,
        total_records,
        successful_records,
        failed_records
    )

    display_metrics(metrics)
    save_metrics(metrics)