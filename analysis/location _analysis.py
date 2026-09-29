import pandas as pd

# Load cleaned dataset
file_path =r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_cleaned.csv"
df = pd.read_csv(file_path)

print("Location-wise Weather Analysis")
print("------------------------------")

# Number of observations for each location
print("\nRecords by Location:")
print(df["location"].value_counts())

# Average weather conditions by location
location_weather = df.groupby("location")[
    [
        "temp_max_c",
        "temp_min_c",
        "rainfall_mm",
        "humidity_pct",
        "wind_speed_kmph"
    ]
].mean()

print("\nAverage Weather Conditions by Location:")
print(location_weather)

# Minimum and maximum temperature by location
temperature_summary = df.groupby("location")[
    ["temp_max_c", "temp_min_c"]
].agg(["min", "max"])

print("\nTemperature Summary by Location:")
print(temperature_summary)
