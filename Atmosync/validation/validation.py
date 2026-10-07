import pandas as pd


# Required columns
REQUIRED_COLUMNS = [
    "date",
    "location",
    "latitude",
    "longitude",
    "elevation_m",
    "area_profile",
    "temp_max_c",
    "temp_min_c",
    "rainfall_mm",
    "humidity_pct",
    "wind_speed_kmph"
]


def validate_data(df):
    """
    Validate AtmoSync micro-climate dataset.
    """

    errors = []

    # Check required columns
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        errors.append(
            f"Missing columns: {missing_columns}"
        )

    if errors:
        return False, errors

    # Check missing values
    missing_values = df[REQUIRED_COLUMNS].isnull().sum()

    for column, count in missing_values.items():
        if count > 0:
            errors.append(
                f"{column} contains {count} missing values"
            )

    # Check humidity range
    if ((df["humidity_pct"] < 0) |
            (df["humidity_pct"] > 100)).any():
        errors.append(
            "Humidity must be between 0 and 100"
        )

    # Check rainfall
    if (df["rainfall_mm"] < 0).any():
        errors.append(
            "Rainfall cannot be negative"
        )

    # Check wind speed
    if (df["wind_speed_kmph"] < 0).any():
        errors.append(
            "Wind speed cannot be negative"
        )

    # Check temperature consistency
    if (df["temp_max_c"] < df["temp_min_c"]).any():
        errors.append(
            "Maximum temperature cannot be lower than minimum temperature"
        )

    if errors:
        return False, errors

    return True, ["Dataset validation successful"]


if __name__ == "__main__":

    # Change this path if your dataset has another name
    file_path = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\data_loading\atmosync_microclimate_raw.csv"

    df = pd.read_csv(file_path)

    valid, messages = validate_data(df)

    for message in messages:
        print(message)

    if valid:
        print("\nData validation PASSED.")
    else:
        print("\nData validation FAILED.")