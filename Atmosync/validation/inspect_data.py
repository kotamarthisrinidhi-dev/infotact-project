import pandas as pd
from pathlib import Path

DATA_FILE = Path( r"C:\Users\rohit\OneDrive\Desktop\atmosync project\data_loading\atmosync_microclimate_raw.csv"
)


def inspect_data():

    print("=" * 50)
    print("AtmoSync Data Inspection")
    print("=" * 50)

    if not DATA_FILE.exists():
        print(f"Dataset not found: {DATA_FILE}")
        return

    df = pd.read_csv(DATA_FILE)

    print(f"\nDataset: {DATA_FILE}")
    print(f"Records: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\nColumns:")
    for column in df.columns:
        print(f"- {column}")

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Records:")
    print(df.duplicated().sum())

    print("\nFirst 5 Records:")
    print(df.head())


if __name__ == "__main__":
    inspect_data()