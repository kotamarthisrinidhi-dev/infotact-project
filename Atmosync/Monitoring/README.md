# AtmoSync Monitoring

The Monitoring module provides observability and health monitoring
for the AtmoSync weather data pipeline.

## Purpose

The monitoring layer helps track the health, execution,
performance, and reliability of the AtmoSync pipeline.

## Monitoring Components

- Pipeline logging
- Health checks
- Pipeline metrics
- Monitoring alerts
- Service availability
- Kafka monitoring
- Snowflake monitoring
- Failure and error tracking
- Final monitoring validation

## Pipeline Components Monitored

```text
Weather Data
     ↓
   Kafka
     ↓
 Snowflake
     ↓
Data Validation
     ↓
    dbt
     ↓
 Dashboard