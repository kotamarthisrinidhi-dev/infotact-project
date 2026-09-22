
# AtmoSync Data Validation

## Purpose

This document defines basic validation checks for the AtmoSync micro-climate dataset before analysis.

## 1. Date Validation

- Check that the date column contains valid date values.
- Check for invalid or missing dates.

## 2. Location Validation

- Check that location values are available.
- Check for unexpected or empty location values.

## 3. Geographic Validation

The following fields should contain numerical values:

- latitude
- longitude
- elevation_m

## 4. Temperature Validation

Check the following weather fields:

- temp_max_c
- temp_min_c

The values should be numerical and consistent.

## 5. Rainfall Validation

Check:

- rainfall_mm

The field should contain numerical rainfall measurements.

## 6. Humidity Validation

Check:

- humidity_pct

Humidity values should be numerical and should be reviewed for unusual values.

## 7. Wind Speed Validation

Check:

- wind_speed_kmph

Wind speed should contain numerical measurements.

## 8. Duplicate Check

Check the dataset for duplicate records before analysis.

## 9. Missing Value Check

Check all columns for missing values.

## 10. Final Validation

After completing the validation checks, the dataset can be prepared for further analysis and visualization.



