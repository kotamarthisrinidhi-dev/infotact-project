# AtmoSync Visualization Testing

## Purpose

This document defines basic testing checks for the visualizations created from the AtmoSync micro-climate dataset.

## 1. Dataset Check

Verify that the cleaned dataset is available at:
r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_cleaned.csv"
## 2. Temperature Chart Check

Verify that the temperature visualization uses:

- temp_max_c
- temp_min_c
- date

Check that:

- Chart is displayed correctly
- X-axis represents date
- Y-axis represents temperature in Celsius
- Legend is available

## 3. Rainfall Chart Check

Verify that the rainfall visualization uses:

- rainfall_mm
- location

Check that:

- Locations are displayed correctly
- Rainfall values are numerical
- Chart title and axis labels are clear

## 4. Humidity Chart Check

Verify that the humidity visualization uses:

- humidity_pct
- location

Check that:

- Humidity values are displayed correctly
- Location comparison is visible
- Axis labels are clear

## 5. Wind Speed Chart Check

Verify that the wind speed visualization uses:

- wind_speed_kmph
- location

Check that:

- Wind speed values are displayed correctly
- Locations are visible
- Units are mentioned

## 6. Correlation Visualization Check

Verify that the correlation visualization includes the main weather parameters:

- Temperature
- Rainfall
- Humidity
- Wind speed

Check that the correlation values are displayed correctly.

## 7. Final Visualization Check

Before using the charts in the dashboard, verify:

- No Python errors
- No missing charts
- Titles are clear
- Axis labels are correct
- Units are displayed
- Charts are readable

## Final Objective

These checks help ensure that AtmoSync visualizations are accurate, readable, and ready for dashboard integration.
