import pandas as pd
from pathlib import Path
from datetime import datetime

INPUT_FILE = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_transformed.csv"
OUTPUT_FILE = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\final_quality_summary.csv"


def generate_quality_summary():

    if not Path(INPUT_FILE).exists():
        print(f"Dataset not found: {INPUT_FILE}")
        return

    df = pd.read_csv(INPUT_FILE)

    if df.empty:
        print("Dataset is empty.")
        return

    summary = {
        "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_records": len(df),
        "duplicate_records": int(df.duplicated().sum()),
        "missing_values": int(df.isnull().sum().sum()),
        "invalid_humidity": int(
            ((df["humidity_pct"] < 0) |
             (df["humidity_pct"] > 100)).sum()
        ),
        "invalid_rainfall": int(
            (df["rainfall_mm"] < 0).sum()
        ),
        "invalid_wind_speed": int(
            (df["wind_speed_kmph"] < 0).sum()
        ),
        "invalid_temperature": int(
            (df["temp_max_c"] < df["temp_min_c"]).sum()
        )
    }

    summary_df = pd.DataFrame([summary])

    summary_df.to_csv(OUTPUT_FILE, index=False)

    print("=" * 45)
    print("AtmoSync Data Quality Summary")
    print("=" * 45)

    for key, value in summary.items():
        print(f"{key}: {value}")

    print("\nQuality summary generated successfully.")


if __name__ == "__main__":
    generate_quality_summary()