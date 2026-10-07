import pandas as pd

# Load cleaned dataset
file_path = "../processed/atmosync_microclimate_cleaned.csv"
df = pd.read_csv(file_path)

# Humidity analysis
print("Humidity Analysis")
print("------------")

# Basic statistics
print("\nAverage Humidity:")
print(df["humidity_pct"].mean())

print("\nMinimum Humidity:")
print(df["humidity_pct"].min())

print("\nMaximum Humidity:")
print(df["humidity_pct"].max())

# Location-wise humidity analysis
location_humidity = (
    df.groupby("location")["humidity_pct"]
    .agg(["mean", "min", "max"])
)

print("\nHumidity by Location:")
print(location_humidity)

# Date-wise humidity analysis
daily_humidity = df.groupby("date")["humidity_pct"].mean()

print("\nDaily Average Humidity:")
print(daily_humidity.head(10))