# AtmoSync Dashboard Data Requirements

## Purpose

This document defines the data fields and metrics required for the AtmoSync dashboard.

## Dataset

The dashboard will use the cleaned dataset:

text
dataset/processed/atmosync_microclimate_cleaned.csv
`

## 1. Location Information

The dashboard can use:

* `location`
* `latitude`
* `longitude`
* `elevation_m`
* `area_profile`

## 2. Weather Parameters

The main weather parameters are:

* `temp_max_c`
* `temp_min_c`
* `rainfall_mm`
* `humidity_pct`
* `wind_speed_kmph`

## 3. Date Information

The dashboard should use:

* `date`

for date-based analysis and filtering.

## 4. Summary Metrics

The dashboard can display:

* Average maximum temperature
* Average minimum temperature
* Average rainfall
* Average humidity
* Average wind speed

## 5. Location Comparison

Users should be able to compare weather parameters between different locations.

## 6. Charts

The dashboard can include:

* Temperature chart
* Rainfall chart
* Humidity chart
* Wind speed chart
* Location comparison chart

## 7. Filters

Possible dashboard filters include:

* Location
* Date

## Final Objective

These data requirements will help organize the cleaned AtmoSync dataset for interactive dashboard development.

`
