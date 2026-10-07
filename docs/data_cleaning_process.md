
# AtmoSync Data Cleaning Process

## Purpose

The data cleaning process prepares the AtmoSync micro-climate dataset for analysis and visualization.

## 1. Load Raw Dataset

The original AtmoSync dataset is loaded from the raw dataset folder.

```text
dataset/raw/atmosync_microclimate_raw.csv
````

## 2. Missing Value Handling

The dataset is checked for missing values.

* Numerical columns are handled using an appropriate numerical replacement method.
* Categorical columns are handled using an appropriate categorical replacement method.

## 3. Date Cleaning

The `date` column is converted into a proper date format.

Invalid date values are identified during the cleaning process.

## 4. Data Type Conversion

Numerical columns are converted into suitable numerical data types.

Important numerical fields include:

* latitude
* longitude
* elevation_m
* temp_max_c
* temp_min_c
* rainfall_mm
* humidity_pct
* wind_speed_kmph

## 5. Duplicate Removal

The dataset is checked for duplicate records.

Duplicate records are removed from the processed dataset.

## 6. Cleaned Dataset

The cleaned dataset is stored separately from the raw dataset.

```text
dataset/processed/atmosync_microclimate_cleaned.csv
```

The original raw dataset remains unchanged.

## 7. Final Verification

After cleaning, the dataset is checked again for:

* Missing values
* Duplicate records
* Correct data types
* Valid date values
* Unusual weather values

## Final Objective

The cleaned dataset is prepared for exploratory data analysis, visualization, and dashboard development.
