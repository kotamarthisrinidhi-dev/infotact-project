# AtmoSync Data Validation

This module validates the quality and consistency
of weather data used in the AtmoSync pipeline.

## Purpose

The validation layer checks weather data before
cleaning and transformation.

## Validation Areas

- Required columns
- Missing values
- Data types
- Temperature consistency
- Humidity range
- Rainfall values
- Wind speed values

## Pipeline

Raw Data
   ↓
Validation
   ↓
Cleaning
   ↓
Transformation
   ↓
Analytics
