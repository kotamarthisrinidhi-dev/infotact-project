import pandas as pd

INPUT_FILE = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\data_loading\atmosync_microclimate_raw.csv"
OUTPUT_FILE = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_transformed.csv"

def transform_data():


    print("Loading cleaned dataset...")

    df = pd.read_csv(INPUT_FILE)

    if df.empty:
        print("Dataset is empty.")
        return

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()

    # Convert date
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Standardize text fields
    df["location"] = df["location"].str.strip().str.title()
    df["area_profile"] = df["area_profile"].str.strip().str.title()

    # Calculate temperature range
    df["temp_range_c"] = (
        df["temp_max_c"] - df["temp_min_c"]
    ).round(2)

    # Calculate average temperature
    df["temp_avg_c"] = (
        (df["temp_max_c"] + df["temp_min_c"]) / 2
    ).round(2)

    # Classify rainfall
    def rainfall_category(value):
        if value == 0:
            return "No Rain"
        elif value <= 2.5:
            return "Light"
        elif value <= 10:
            return "Moderate"
        else:
            return "Heavy"

    df["rainfall_category"] = df["rainfall_mm"].apply(
        rainfall_category
    )

    # Classify humidity
    def humidity_category(value):
        if value < 30:
            return "Low"
        elif value <= 60:
            return "Moderate"
        else:
            return "High"

    df["humidity_category"] = df["humidity_pct"].apply(
        humidity_category
    )

    # Save transformed dataset
    df.to_csv(OUTPUT_FILE, index=False)

    print("\nTransformation completed successfully.")
    print(f"Records processed: {len(df)}")
    print(f"Output file: {OUTPUT_FILE}")

    print("\nNew fields:")
    print("- temp_range_c")
    print("- temp_avg_c")
    print("- rainfall_category")
    print("- humidity_category")


if __name__ == "__main__":
    transform_data()