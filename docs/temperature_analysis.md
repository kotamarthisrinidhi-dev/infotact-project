# AtmoSync Temperature Analysis

## Purpose

This document describes the temperature analysis planned for the AtmoSync micro-climate dataset.

## Temperature Fields

The main temperature columns are:

- `temp_max_c` – Maximum temperature in Celsius
- `temp_min_c` – Minimum temperature in Celsius

## 1. Average Temperature

Calculate the average maximum and minimum temperature from the dataset.

## 2. Temperature Range

Calculate the difference between maximum and minimum temperature.

```text
temperature_range = temp_max_c - temp_min_c
````

## 3. Minimum and Maximum Values

Identify:

* Lowest recorded maximum temperature
* Highest recorded maximum temperature
* Lowest recorded minimum temperature
* Highest recorded minimum temperature

## 4. Location-wise Temperature Analysis

Compare average maximum and minimum temperatures across different locations.

## 5. Temperature Patterns

Use the `date` field to study changes in temperature over time.

## 6. Visualization

Temperature analysis can be represented using:

* Line charts
* Bar charts
* Histograms
* Box plots

## Expected Output

The analysis should provide:

* Average maximum temperature
* Average minimum temperature
* Temperature range
* Minimum and maximum temperature values
* Location-wise temperature comparison
* Temperature patterns over time

## Final Objective

The temperature analysis will help understand how temperature varies across locations and over time in the AtmoSync micro-climate dataset.
