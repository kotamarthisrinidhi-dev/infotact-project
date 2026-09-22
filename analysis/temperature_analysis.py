import pandas as pd

# Load cleaned dataset
file_path = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_cleaned.csv"
df = pd.read_csv(file_path)

# Temperature columns
temperature_columns = [
    "temp_max_c",
    "temp_min_c"
]

# Basic temperature statistics
print("Temperature Analysis")
print("--------------------")

for column in temperature_columns:
    print(f"\n{column}")
    print("Average:", df[column].mean())
    print("Minimum:", df[column].min())
    print("Maximum:", df[column].max())

# Location-wise temperature analysis
location_temperature = df.groupby("location")[
    ["temp_max_c", "temp_min_c"]
].mean()

print("\nAverage Temperature by Location:")
print(location_temperature)

# Temperature difference
df["temperature_range_c"] = (
    df["temp_max_c"] - df["temp_min_c"]
)

print("\nAverage Temperature Range:")
print(df["temperature_range_c"].mean())