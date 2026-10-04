import pandas as pd

# Load cleaned dataset
file_path =r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_cleaned.csv"
df = pd.read_csv(file_path)

print("Weather Correlation Analysis")
print("----------------------------")

# Select weather columns
weather_columns = [
    "temp_max_c",
    "temp_min_c",
    "rainfall_mm",
    "humidity_pct",
    "wind_speed_kmph"
]

# Calculate correlation matrix
correlation_matrix = df[weather_columns].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

# Display strong positive/negative relationships
print("\nCorrelation Analysis Completed.")