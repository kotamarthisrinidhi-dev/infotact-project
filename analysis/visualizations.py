import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
file_path =r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_cleaned.csv"
df = pd.read_csv(file_path)

# 1. Temperature Visualization
plt.figure(figsize=(10, 5))

plt.plot(df[ "date" ], df["temp_max_c"], label="Max Temperature")
plt.plot(df[ "date" ], df["temp_min_c"], label="Min Temperature")

plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trends")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# 2. Rainfall Visualization

rainfall_by_location = df.groupby("location")["rainfall_mm"].mean()

plt.figure(figsize=(10, 5))

rainfall_by_location.plot(kind="bar")

plt.xlabel("Location")
plt.ylabel("Average Rainfall (mm)")
plt.title("Average Rainfall by Location")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Humidity Visualization

humidity_by_location = df.groupby("location")["humidity_pct"].mean()

plt.figure(figsize=(10, 5))

humidity_by_location.plot(kind="bar")

plt.xlabel("Location")
plt.ylabel("Average Humidity (%)")
plt.title("Average Humidity by Location")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Wind Speed Visualization

wind_by_location = df.groupby("location")["wind_speed_kmph"].mean()

plt.figure(figsize=(10, 5))

wind_by_location.plot(kind="bar")

plt.xlabel("Location")
plt.ylabel("Average Wind Speed (km/h)")
plt.title("Average Wind Speed by Location")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print("Weather visualizations created successfully.")