import pandas as pd
from pathlib import Path

INPUT_FILE = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_transformed.csv"


def run_final_test():

    print("=" * 50)
    print("AtmoSync Final Data Quality Test")
    print("=" * 50)

    if not Path(INPUT_FILE).exists():
        print("FAIL: Transformed dataset not found.")
        return

    df = pd.read_csv(INPUT_FILE)

    if df.empty:
        print("FAIL: Dataset is empty.")
        return

    errors = []

    # Required columns
    required_columns = [
        "date",
        "location",
        "latitude",
        "longitude",
        "temp_max_c",
        "temp_min_c",
        "rainfall_mm",
        "humidity_pct",
        "wind_speed_kmph"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        errors.append(f"Missing columns: {missing_columns}")

    # Missing values
    if df[required_columns].isnull().sum().sum() > 0:
        errors.append("Missing values detected.")

    # Temperature
    if (df["temp_max_c"] < df["temp_min_c"]).any():
        errors.append("Invalid temperature values.")

    # Humidity
    if ((df["humidity_pct"] < 0) |
            (df["humidity_pct"] > 100)).any():
        errors.append("Invalid humidity values.")

    # Rainfall
    if (df["rainfall_mm"] < 0).any():
        errors.append("Negative rainfall detected.")

    # Wind
    if (df["wind_speed_kmph"] < 0).any():
        errors.append("Negative wind speed detected.")

    # Coordinates
    if ((df["latitude"] < -90) |
            (df["latitude"] > 90)).any():
        errors.append("Invalid latitude values.")

    if ((df["longitude"] < -180) |
            (df["longitude"] > 180)).any():
        errors.append("Invalid longitude values.")

    # Duplicates
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        errors.append(
            f"{duplicates} duplicate records detected."
        )

    print(f"Records tested: {len(df)}")
    print(f"Duplicates: {duplicates}")

    if errors:
        print("\nFINAL QUALITY TEST: FAILED")

        for error in errors:
            print(f"- {error}")

    else:
        print("\nFINAL QUALITY TEST: PASSED")
        print("Dataset is ready for downstream processing.")


if __name__ == "__main__":
    run_final_test()