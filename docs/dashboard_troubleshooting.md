

# AtmoSync Dashboard Troubleshooting Guide

## Purpose

This guide describes common issues that may occur while running the AtmoSync dashboard and provides possible solutions.

## 1. Streamlit Not Installed

**Problem:** The terminal reports that Streamlit is not installed or the command is not recognized.

**Solution:**

```
pip install streamlit
```

## 2. Dataset Not Found

**Problem:** The dashboard cannot find the cleaned dataset.

**Expected path:**

`r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_cleaned.csv"`

**Solution:**

* Verify the file exists.

* Run the data-cleaning script if the processed dataset has not been created.

* Run the dashboard from the project root directory.

## 3. Missing Python Packages

**Problem:** Python reports that a required package is missing.

**Solution:**

```
pip install -r requirements.txt
```

## 4. Missing Dataset Columns

**Problem:** The dashboard reports a missing column error.

**Solution:**

Verify that the dataset contains the required columns:

* `date`

* `location`

* `temp_max_c`

* `temp_min_c`

* `rainfall_mm`

* `humidity_pct`

* `wind_speed_kmph`

## 5. Dashboard Does Not Start

**Problem:** The dashboard fails to launch.

**Solution:**

Run the command from the project root:

```
streamlit run dashboard/app.py
```

Check the terminal for error messages and resolve them before trying again.

## 6. Empty or Unexpected Results

**Problem:** The dashboard displays empty charts or unexpected values.

**Solution:**

* Check whether the dataset contains records.

* Verify the selected filters, if available.

* Check for missing or invalid values in the relevant columns.

* Confirm that the dashboard uses the correct dataset path.

## 7. General Troubleshooting Checklist

* Python is installed.

* Required packages are installed.

* The cleaned dataset exists.

* Dataset columns are correct.

* The dashboard starts without errors.

* Metrics and charts display expected results.

## Conclusion

This guide helps team members identify and resolve common AtmoSync dashboard issues during development and testing.
