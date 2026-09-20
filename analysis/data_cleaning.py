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