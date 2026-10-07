import pandas as pd
from pathlib import Path

INPUT_FILE = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_transformed.csv"


def final_validation():

    if not Path(INPUT_FILE).exists():
        print(f"Dataset not found: {INPUT_FILE}")
        return

    df = pd.read_csv(INPUT_FILE)

    if df.empty:
        print("Dataset is empty.")
        return

    print("=" * 45)
    print("AtmoSync Final Dataset Validation")
    print("=" * 45)

    errors = []

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

    # Check required columns
    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        errors.append(
            f"Missing columns: {missing_columns}"
        )

    # Check missing values
    missing_values = df[required_columns].isnull().sum()

    if missing_values.sum() > 0:
        errors.append("Missing values detected in required columns.")

    # Weather validations
    if (df["temp_max_c"] < df["temp_min_c"]).any():
        errors.append("Invalid temperature relationship detected.")

    if ((df["humidity_pct"] < 0) |
            (df["humidity_pct"] > 100)).any():
        errors.append("Invalid humidity values detected.")

    if (df["rainfall_mm"] < 0).any():
        errors.append("Negative rainfall detected.")

    if (df["wind_speed_kmph"] < 0).any():
        errors.append("Negative wind speed detected.")

    # Duplicate check
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        errors.append(
            f"{duplicates} duplicate records detected."
        )

    print(f"Records checked: {len(df)}")
    print(f"Columns available: {len(df.columns)}")
    print(f"Duplicate records: {duplicates}")

    if not errors:
        print("\nFINAL VALIDATION PASSED")
        print("Dataset is ready for downstream processing.")
    else:
        print("\nFINAL VALIDATION FAILED")

        for error in errors:
            print(f"- {error}")


if __name__ == "__main__":
    final_validation()