import pandas as pd


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


def clean_data(df):
    """
    Clean the AtmoSync micro-climate dataset.
    """

    # Make a copy so the original data is not modified
    df = df.copy()

    # Remove duplicate records
    df = df.drop_duplicates()

    # Convert date column
    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    # Convert numeric columns
    numeric_columns = [
        "latitude",
        "longitude",
        "elevation_m",
        "temp_max_c",
        "temp_min_c",
        "rainfall_mm",
        "humidity_pct",
        "wind_speed_kmph"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # Remove records with missing required values
    df = df.dropna(subset=REQUIRED_COLUMNS)

    # Remove invalid humidity values
    df = df[
        (df["humidity_pct"] >= 0) &
        (df["humidity_pct"] <= 100)
    ]

    # Remove negative rainfall
    df = df[df["rainfall_mm"] >= 0]

    # Remove negative wind speed
    df = df[df["wind_speed_kmph"] >= 0]

    # Ensure maximum temperature >= minimum temperature
    df = df[
        df["temp_max_c"] >= df["temp_min_c"]
    ]

    return df


if __name__ == "__main__":

    input_file = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\data_loading\atmosync_microclimate_raw.csv"
    output_file = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_cleaned.csv"

    df = pd.read_csv(input_file)

    print(f"Original records: {len(df)}")

    cleaned_df = clean_data(df)

    print(f"Clean records: {len(cleaned_df)}")
    print(
        f"Removed records: "
        f"{len(df) - len(cleaned_df)}"
    )

    cleaned_df.to_csv(
        output_file,
        index=False
    )

    print(f"\nClean dataset saved to: {output_file}")