

# AtmoSync Dashboard User Guide

## 1. Introduction

The AtmoSync dashboard is designed to explore micro-climate weather data through summary metrics, charts, and location-based information.

## 2. Dashboard Requirements

The dashboard requires:

* Python

* Streamlit

* Pandas

* The processed AtmoSync dataset

## 3. Dataset Location

The dashboard uses the cleaned dataset stored at:

`dataset/processed/atmosync_microclimate_cleaned.csv`

## 4. Starting the Dashboard

Open a terminal in the project root directory and run:

```
streamlit run dashboard/app.py
```

The dashboard will open in a browser.

## 5. Dataset Overview

The overview section displays information such as:

* Total records

* Total columns

* Number of locations

## 6. Weather Summary

The dashboard can display summary metrics such as:

* Average maximum temperature

* Average minimum temperature

* Average rainfall

* Average humidity

* Average wind speed

The metrics shown depend on the implemented dashboard features.

## 7. Exploring Weather Data

Users can review the displayed dataset to understand the available dates, locations, and weather parameters.

When filters and charts are available, users can use them to explore selected data.

## 8. Troubleshooting

### Dashboard does not start

Verify that Streamlit is installed:

```
pip install streamlit pandas
```

### Dataset not found

Check that the cleaned dataset exists at the expected path.

If it does not exist, run the project's data-cleaning script first.

### Missing column error

Verify that the dataset contains the columns required by the dashboard.

## 9. Conclusion

This guide helps users launch the AtmoSync dashboard and understand its main features.
