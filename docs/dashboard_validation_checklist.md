# AtmoSync Dashboard Validation Checklist

# 1. Dataset Validation

-  Cleaned dataset exists at the expected path.
-  Required columns are available.
-  Date and numeric columns are validated.
-  Missing values are reviewed.
-  Duplicate records are reviewed.

# 2. Summary Metrics

- Total record count matches the loaded dataset.
- Location count matches unique locations.
- Average maximum temperature is calculated correctly.
- Average minimum temperature is calculated correctly.
- Average rainfall is calculated correctly.
- Average humidity is calculated correctly.
- Average wind speed is calculated correctly.

# 3. Visualization Validation

- Temperature trend displays valid dates and values.
- Rainfall chart displays location-wise values.
- Humidity chart displays location-wise values.
- Wind-speed chart displays location-wise values.
- Charts update when filters are changed.

# 4. Filter Validation

- Single-location selection works correctly.
- Multiple-location selection works correctly.
- All-location selection works correctly.
- Empty filter selection is handled correctly.
- KPI values update after filtering.
- Charts use the filtered dataset.

# 5. Error Handling

- Missing dataset displays a clear error message.
- Missing required columns display a clear error message.
- Empty filtered results display a warning.
- Missing chart values do not break the dashboard.

 6. Results

Record each test as:
- Pass
- Fail
- Not Tested
Do not mark a test as Pass without actually verifying it.
