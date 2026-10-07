
# AtmoSync Data Cleaning Summary

## Purpose

This document summarizes the data cleaning activities performed on the AtmoSync micro-climate dataset.

## Cleaning Activities

### 1. Missing Value Check

The dataset was checked for missing values in all columns.

### 2. Date Conversion

The `date` column was converted into a proper date format.

### 3. Numerical Data Conversion

The following columns were converted to numerical data types:

- latitude
- longitude
- elevation_m
- temp_max_c
- temp_min_c
- rainfall_mm
- humidity_pct
- wind_speed_kmph

### 4. Duplicate Check

Duplicate records were identified and removed from the processed dataset.

### 5. Outlier Check

Weather-related columns were checked for unusual values using the IQR method.

The outlier analysis does not automatically remove values.

## Raw and Processed Dataset

The original raw dataset is preserved in:

```text
dataset/raw/
````

The cleaned dataset is stored in:

```text
dataset/processed/
```

## Final Purpose

The cleaned dataset is used as the input for further exploratory data analysis, visualization, and dashboard development.

