import pandas as pd

# Dataset path
file_path = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\data_loading\atmosync_microclimate_raw.csv"

# Load dataset
df = pd.read_csv(file_path)

# Dataset shape
print("Dataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Basic information
print("\nDataset Information:")
df.info()
