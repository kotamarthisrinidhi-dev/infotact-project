import pandas as pd
from pathlib import Path

INPUT_FILE = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_transformed.csv"


def validate_weather_data():

    if not Path(INPUT_FILE).exists():
        print(f"Dataset not found: {INPUT_FILE}")
        return

    df = pd.read_csv(INPUT_FILE)

    if df.empty:
        print("Dataset is empty.")
        return

    print("AtmoSync Advanced Data Validation")
    print("=" * 40)

    errors = []

    # Temperature validation
    if (df["temp_max_c"] < df["temp_min_c"]).any():
        errors.append("Maximum temperature is lower than minimum temperature.")

    # Humidity validation
    if ((df["humidity_pct"] < 0) |
        (df["humidity_pct"] > 100)).any():
        errors.append("Humidity contains values outside 0-100%.")

    # Rainfall validation
    if (df["rainfall_mm"] < 0).any():
        errors.append("Negative rainfall values detected.")

    # Wind validation
    if (df["wind_speed_kmph"] < 0).any():
        errors.append("Negative wind-speed values detected.")

    # Coordinates
    if ((df["latitude"] < -90) |
        (df["latitude"] > 90)).any():
        errors.append("Invalid latitude detected.")

    if ((df["longitude"] < -180) |
        (df["longitude"] > 180)).any():
        errors.append("Invalid longitude detected.")

    # Duplicate validation
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        errors.append(
            f"{duplicates} duplicate records detected."
        )

    print()

    if not errors:
        print("VALIDATION PASSED")
        print("No critical data-quality issues detected.")
    else:
        print("VALIDATION FAILED")

        for error in errors:
            print(f"- {error}")

    print()
    print(f"Records checked: {len(df)}")


if __name__ == "__main__":
    validate_weather_data()