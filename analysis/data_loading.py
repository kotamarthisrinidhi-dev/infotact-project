import pandas as pd

# Path to the raw dataset
file_path = "../raw/dataset/atmosync_microclimate_raw.csv"

# Load the dataset
df = pd.read_csv(file_path)

# Verify dataset loading
print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

# Display first 5 records
print("\nFirst 5 records:")
print(df.head())
