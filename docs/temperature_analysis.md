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
