import pandas as pd

# Dataset path
file_path = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\data_loading\atmosync_microclimate_raw.csv"


# Load dataset
df = pd.read_csv(file_path)

# Check missing values before cleaning
print("Missing Values Before Cleaning:")
print(df.isnull().sum())

# Fill missing numerical values with median
numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].median())

# Fill missing categorical values with mode
categorical_columns = df.select_dtypes(include=["object"]).columns

for column in categorical_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].mode()[0])
# Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
output_path = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_cleaned.csv"
df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully.")

# -----------------------------
# 6. Clean Date and Data Types
# -----------------------------

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Numerical columns
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

# Convert numerical columns to numeric datatype
for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Display data types after conversion
print("\nData Types After Cleaning:")
print(df.dtypes)

# Check invalid/missing dates
print("\nInvalid or Missing Dates:")
print(df["date"].isnull().sum())
# -----------------------------
# 7. Check Duplicate Records
# -----------------------------

# Count duplicates before removal
duplicates_before = df.duplicated().sum()

print("\nDuplicate Records Before Cleaning:")
print(duplicates_before)

# Remove duplicate records
df = df.drop_duplicates()

# Count duplicates after removal
duplicates_after = df.duplicated().sum()

print("\nDuplicate Records After Cleaning:")
print(duplicates_after)

# Display dataset shape after duplicate removal
print("\nDataset Shape After Duplicate Removal:")
print(df.shape)

# -----------------------------
# 8. Save Cleaned Dataset
# -----------------------------

output_path = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully.")