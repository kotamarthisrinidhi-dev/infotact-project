# AtmoSync Rainfall Analysis Testing

## Purpose

This document defines basic checks for the rainfall analysis in the AtmoSync project.

## 1. Rainfall Column Check

Verify that the following column is available:

- `rainfall_mm`

## 2. Data Type Check

Verify that `rainfall_mm` contains numerical values.

## 3. Missing Value Check

Check whether rainfall values contain missing records.

## 4. Statistical Checks

Verify that the analysis calculates:

- Average rainfall
- Minimum rainfall
- Maximum rainfall
- Total rainfall

## 5. Location-wise Check

Verify that rainfall values can be grouped and compared by:

- `location`

## 6. Date-wise Check

Verify that rainfall values can be analyzed using:

- `date`

## 7. Output Check

The rainfall analysis should run without errors and display the expected results.

## Final Objective

These checks help verify that rainfall analysis is working correctly before the results are used for visualization and dashboard development.
