import pandas as pd

# Load cleaned dataset

file_path = r"C:\Users\rohit\OneDrive\Desktop\atmosyncproject\processed\atmosync_microclimate_cleaned.csv" 
df = pd.read_csv(file_path)

# Humidity analysis

print("Humidity Analysis")
print("------------")

000

# Basic statistics

print("\nAverage Humidity:")
print(df["humidity_pct"].me an())

print("\nMinimum Humidity:") 
print(df["humidity_pct"].mi n())

print("\nMaximum Humidity:") 
print(df["humidity_pct"].ma x())

# Location-wise humidity analysis
location_humidity = df.groupby("location") ["humidity_pct"].agg(["mean", "min", "max"])

print("\nHumidity by Location:") 
print(location_humidity)

# Date-wise humidity analysis
daily_humidity = df.groupby("date") ["humidity_pct"].mean()

print("\nDaily Average Humidity:")
print(daily_humidity.head (1 0))
