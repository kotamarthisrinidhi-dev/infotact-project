import json
from pathlib import Path
from datetime import datetime

ERROR_FILE = "logs/pipeline_errors.json"


def log_error(component, error_message):
    Path("logs").mkdir(exist_ok=True)

    errors = []

    if Path(ERROR_FILE).exists():
        try:
            with open(ERROR_FILE, "r") as file:
                errors = json.load(file)
        except (json.JSONDecodeError, OSError):
            errors = []

    errors.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "component": component,
        "error": str(error_message)
    })

    with open(ERROR_FILE, "w") as file:
        json.dump(errors, file, indent=4)


def show_errors():
    if not Path(ERROR_FILE).exists():
        print("No pipeline errors recorded.")
        return

    with open(ERROR_FILE, "r") as file:
        errors = json.load(file)

    print("=" * 45)
    print("AtmoSync Pipeline Error Report")
    print("=" * 45)

    if not errors:
        print("No errors recorded.")
        return

    for error in errors:
        print(f"Time      : {error['timestamp']}")
        print(f"Component : {error['component']}")
        print(f"Error     : {error['error']}")
        print("-" * 45)


if __name__ == "__main__":
    show_errors()