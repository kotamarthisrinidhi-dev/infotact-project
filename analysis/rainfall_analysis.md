import pandas as pd

# Load cleaned dataset file_path =r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_cleaned.csv"
df = pd.read_csv(file_path)

# Rainfall analysis 24
print("Rainfall Analysis") 
print("------")

print("\nAverage Rainfall:") 
print(df["rainfall_mm"].mea n())

print("\nMinimum Rainfall:") 
print(df["rainfall_mm"].min ())

print("\nMaximum Rainfall:") 
print(df["rainfall_mm"].max ())

print("\nTotal Rainfall:") 
print(df["rainfall_mm"].sum ())


# Location-wise rainfall analysis 
location_rainfall = df.groupby("location") ["rainfall_mm"].agg( ["mean", "min", "max", "sum"] )

print("\nRainfall by Location:") 
print(location_rainfall)

# Date-wise rainfall 
daily_rainfall = df.groupby("date") ["rainfall_mm"].sum()

print("\nDaily Rainfall:") 
print(daily_rainfall.head (1 0))
