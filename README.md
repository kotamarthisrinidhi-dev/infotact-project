# AtmoSync: Micro-Climate Analytics for Location-Level Environmental Intelligence

# Project Overview

AtmoSync is an end-to-end data analytics project designed to analyze micro-climate conditions at the location level.

The project focuses on understanding variations in:

- Temperature
- Rainfall
- Humidity
- Wind speed

across different locations.
The solution follows a complete analytics workflow from raw data preparation and quality assessment to exploratory analysis, validation, visualization, and interactive dashboard development.

---

# Business Problem

Weather conditions can vary between nearby locations. Regional-level weather information may not always represent these local differences accurately.

AtmoSync addresses this problem by analyzing location-level weather observations and converting them into meaningful environmental intelligence.

The project aims to understand:

- Weather variations between locations
- Temperature patterns
- Rainfall differences
- Humidity conditions
- Wind-speed variations
- Relationships between weather variables

---

# Project Objectives

- Load and inspect micro-climate weather data
- Assess data quality
- Handle missing values and duplicate records
- Standardize dates and numerical data
- Identify potential weather-data outliers
- Analyze temperature, rainfall, humidity, and wind patterns
- Compare weather conditions across locations
- Analyze relationships between weather variables
- Develop analytical visualizations
- Build an interactive Streamlit dashboard
- Validate analytical outputs

---

# Dataset

Dataset: atmosync_microclimate_raw.csv

Dataset Size:
- 460 records
- 11 columns

# Dataset Variables

| Column | Description |
|---|---|
| `date` | Weather observation date |
| `location` | Observation location |
| `latitude` | Geographic latitude |
| `longitude` | Geographic longitude |
| `elevation_m` | Elevation in metres |
| `area_profile` | Area classification |
| `temp_max_c` | Maximum temperature |
| `temp_min_c` | Minimum temperature |
| `rainfall_mm` | Rainfall |
| `humidity_pct` | Humidity percentage |
| `wind_speed_kmph` | Wind speed |

---

# Analytics Workflow

  text
Raw Dataset
     ↓
Data Loading
     ↓
Data Inspection
     ↓
Data Cleaning
     ↓
Data Validation
     ↓
Exploratory Data Analysis
     ↓
Statistical Analysis
     ↓
Visualization
     ↓
Analytical Validation
     ↓
Streamlit Dashboard
     ↓
Business Insights



# Data Preparation

The project includes:

- Missing-value handling
- Date standardization
- Numerical data-type validation
- Duplicate record removal
- Outlier assessment using IQR
- Data-quality validation

---

# Analysis Performed

# Temperature Analysis

- Maximum temperature
- Minimum temperature
- Temperature variation
- Daily temperature trends
- Location-wise temperature differences

# Rainfall Analysis

- Average rainfall
- Minimum and maximum rainfall
- Total rainfall
- Location-wise rainfall
- Date-wise rainfall

# Humidity Analysis

- Average humidity
- Minimum and maximum humidity
- Location-wise humidity
- Daily humidity patterns

# Wind Analysis

Wind-speed differences are analyzed across locations.

# Location Analysis

Locations are compared using:

- Temperature
- Rainfall
- Humidity
- Wind speed

# Correlation Analysis

Relationships between major numerical weather variables are analyzed using correlation analysis.

---

# Dashboard

The AtmoSync dashboard is developed using **Streamlit** and **Plotly**.

# 1. Executive Command Center

Provides:

- Total records
- Average maximum temperature
- Average minimum temperature
- Average rainfall
- Average humidity
- Temperature trends
- Executive insights

# 2. Location Intelligence

Provides:

- Location-wise temperature comparison
- Rainfall comparison
- Humidity comparison
- Wind-speed comparison
- Location profiles
- Temperature vs. humidity analysis

# 3. Climate & Data Intelligence

Provides:

- Monthly climate patterns
- Metric distributions
- Correlation analysis
- Data-quality indicators
- IQR anomaly analysis
- Filtered data exploration
- CSV export

---

# Dashboard Features

- Location filtering
- Date-range filtering
- Dynamic KPI calculations
- Interactive Plotly charts
- Data-quality validation
- Error handling
- Empty-filter handling
- CSV data download

---

# Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data analysis and development |
| Pandas | Data processing |
| NumPy | Numerical analysis |
| Matplotlib | Visualization |
| Seaborn | Statistical visualization |
| Plotly | Interactive charts |
| Streamlit | Dashboard |
| Git/GitHub | Version control |
