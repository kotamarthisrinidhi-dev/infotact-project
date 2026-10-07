# AtmoSync dbt

This module contains the dbt transformation layer
for the AtmoSync weather analytics pipeline.

## Purpose

dbt is used to transform and validate weather data
stored in Snowflake.

## Data Flow

Kafka
  ↓
Snowflake STAGING
  ↓
Snowflake RAW
  ↓
dbt
  ↓
CLEAN
  ↓
ANALYTICS
  ↓
AtmoSync Dashboard

## Database

ATMOSYNC_DB

## Transformation Layers

- Staging
- Clean
- Analytics
