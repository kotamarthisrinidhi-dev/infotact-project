# AtmoSync Data Validation Configuration

REQUIRED_COLUMNS = [
    "date",
    "location",
    "latitude",
    "longitude",
    "elevation_m",
    "area_profile",
    "temp_max_c",
    "temp_min_c",
    "rainfall_mm",
    "humidity_pct",
    "wind_speed_kmph"
]

print("AtmoSync validation configuration loaded.")
print(f"Required columns: {len(REQUIRED_COLUMNS)}")