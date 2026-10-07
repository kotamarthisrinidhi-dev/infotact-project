import json
from pathlib import Path

METRICS_FILE = Path("logs/pipeline_metrics.json")

MIN_SUCCESS_RATE = 95
MAX_EXECUTION_TIME = 60


def load_metrics():

    if not METRICS_FILE.exists():
        print("Metrics file not found.")
        return None

    with open(METRICS_FILE, "r") as file:
        return json.load(file)


def check_alerts(metrics):

    alerts = []

    success_rate = metrics["success_rate_percent"]
    failed_records = metrics["failed_records"]
    execution_time = metrics["execution_time_seconds"]

    if success_rate < MIN_SUCCESS_RATE:
        alerts.append(
            f"Low success rate: {success_rate}%"
        )

    if failed_records > 0:
        alerts.append(
            f"Failed records detected: {failed_records}"
        )

    if execution_time > MAX_EXECUTION_TIME:
        alerts.append(
            f"Pipeline execution time is high: "
            f"{execution_time} seconds"
        )

    return alerts


def main():

    print("==============================")
    print("AtmoSync Pipeline Alerts")
    print("==============================")

    metrics = load_metrics()

    if metrics is None:
        print("Unable to perform alert checks.")
        return

    alerts = check_alerts(metrics)

    if not alerts:

        print("STATUS: HEALTHY")
        print("No monitoring alerts detected.")

    else:

        print("STATUS: ATTENTION REQUIRED")

        print("\nAlerts:")

        for alert in alerts:
            print(f"- {alert}")


if __name__ == "__main__":
    main()