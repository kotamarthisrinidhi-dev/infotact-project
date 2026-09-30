# AtmoSync Dashboard Testing

## Purpose

This document defines the basic testing checks for the AtmoSync dashboard.

## 1. Dataset Loading

Verify that the dashboard can load:

text
dataset/processed/atmosync_microclimate_cleaned.csv
`

Check:

* Dataset loads without errors
* Required columns are available
* No incorrect file path is used

## 2. Summary Metrics

Verify that the dashboard displays:

* Average maximum temperature
* Average minimum temperature
* Average rainfall
* Average humidity
* Average wind speed

## 3. Location Filter

Check that the location filter:

* Displays available locations
* Allows the user to select a location
* Updates the displayed data correctly

## 4. Date Filter

Check that the date filter:

* Displays valid dates
* Allows date selection
* Updates charts and metrics correctly

## 5. Temperature Charts

Verify:

* Maximum temperature is displayed
* Minimum temperature is displayed
* Chart title is clear
* Temperature unit is shown

## 6. Rainfall Charts

Verify:

* Rainfall values are displayed
* Location comparison works
* Rainfall unit is shown

## 7. Humidity Charts

Verify:

* Humidity values are displayed
* Location comparison works
* Percentage unit is shown

## 8. Wind Speed Charts

Verify:

* Wind speed values are displayed
* Location comparison works
* Wind speed unit is shown

## 9. Error Testing

Check that the dashboard does not produce errors when:

* Dataset is loaded
* Filters are changed
* Different locations are selected
* Different dates are selected

## 10. Final Dashboard Check

Before final submission, verify:

* All charts are visible
* Filters work correctly
* Metrics display correctly
* No Python errors occur
* Text and labels are readable
* Dashboard layout is organized

## Final Objective

The testing process helps ensure that the AtmoSync dashboard is functional, readable, and ready for final project presentation.

`
