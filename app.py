import pandas as pd
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AtmoSync Dashboard",
    page_icon="🌦️",
    layout="wide"
)

# Dashboard title
st.title("🌦️ AtmoSync: Micro-Climate Analytics")
st.write(
    "Explore temperature, rainfall, humidity, and wind speed "
    "across different locations."
)

# Load cleaned dataset
file_path = r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_cleaned.csv"

@st.cache_data
def load_data(path):
    data = pd.read_csv(path)
    data["date"] = pd.to_datetime(data["date"], errors="coerce")
    return data

try:
    df = load_data(file_path)

    # Dataset overview
    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", len(df))
    col2.metric("Total Columns", len(df.columns))
    col3.metric("Locations", df["location"].nunique())

    # Show dataset
    st.subheader("Weather Dataset")
    st.dataframe(df, use_container_width=True)
    
    # Weather summary
    st.subheader("Weather Summary")

    metric_cols = st.columns(4)

    metric_cols[0].metric(
        "Avg Max Temperature",
        f"{df['temp_max_c'].mean():.1f} °C"
    )
    metric_cols[1].metric(
        "Avg Min Temperature",
        f"{df['temp_min_c'].mean():.1f} °C"
    )
    metric_cols[2].metric(
        "Avg Rainfall",
        f"{df['rainfall_mm'].mean():.1f} mm"
    )
    metric_cols[3].metric(
        "Avg Humidity",
        f"{df['humidity_pct'].mean():.1f}%"
    )

except FileNotFoundError:
    st.error(
        "Cleaned dataset not found. "
        "Please run the data cleaning script first."
    )
except KeyError as error:
    st.error(f"Required dataset column is missing: {error}")

    
st.subheader("Weather Visualizations")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Location filter
locations = sorted(df["location"].dropna().unique())
selected_locations = st.multiselect(
    "Select Locations",
    locations,
    default=locations
)

filtered_df = df[df["location"].isin(selected_locations)].copy()

if filtered_df.empty:
    st.warning("No weather data available for the selected locations.")
else:
    # Temperature chart
    st.subheader("Daily Temperature Trends")
    daily_temp = filtered_df.groupby("date")[
        ["temp_max_c", "temp_min_c"]
    ].mean()

    st.line_chart(daily_temp)

    # Rainfall chart
    st.subheader("Average Rainfall by Location")
    rainfall = filtered_df.groupby("location")[
        "rainfall_mm"
    ].mean()

    st.bar_chart(rainfall)

    # Humidity chart
    st.subheader("Average Humidity by Location")
    humidity = filtered_df.groupby("location")[
        "humidity_pct"
    ].mean()

    st.bar_chart(humidity)

    # Wind speed chart
    st.subheader("Average Wind Speed by Location")
    wind = filtered_df.groupby("location")[
        "wind_speed_kmph"
    ].mean()

    st.bar_chart(wind)