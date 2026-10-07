import pandas as pd
from pathlib import Path

INPUT_FILE = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_transformed.csv"
REPORT_FILE = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\validation\data_quality_report.csv"


def generate_quality_report():

    print("Loading transformed dataset...")

    if not Path(INPUT_FILE).exists():
        print(f"Dataset not found: {INPUT_FILE}")
        return

    df = pd.read_csv(INPUT_FILE)

    if df.empty:
        print("Dataset is empty.")
        return

    print(f"Records loaded: {len(df)}")

    report = []

    for column in df.columns:

        missing = df[column].isna().sum()
        unique = df[column].nunique()

        report.append({
            "column": column,
            "data_type": str(df[column].dtype),
            "missing_values": missing,
            "missing_percentage": round(
                (missing / len(df)) * 100, 2
            ),
            "unique_values": unique
        })

    quality_df = pd.DataFrame(report)

    # Duplicate records
    duplicate_count = df.duplicated().sum()

    # Save report
    quality_df.to_csv(REPORT_FILE, index=False)

    print("\n==============================")
    print("AtmoSync Data Quality Report")
    print("==============================")

    print(f"Total records      : {len(df)}")
    print(f"Total columns      : {len(df.columns)}")
    print(f"Duplicate records  : {duplicate_count}")

    print("\nMissing values:")
    print(
        quality_df[
            quality_df["missing_values"] > 0
        ][
            ["column", "missing_values", "missing_percentage"]
        ]
    )

    print("\nQuality report saved successfully.")
    print(f"Output: {REPORT_FILE}")


if __name__ == "__main__":
    generate_quality_report()