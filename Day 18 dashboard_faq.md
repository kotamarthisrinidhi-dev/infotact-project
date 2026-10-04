# AtmoSync Dashboard FAQ

## 1. What is AtmoSync?

AtmoSync is a micro-climate analytics project that explores weather observations across different locations.

## 2. What data does the dashboard display?

It displays temperature, rainfall, humidity, and wind-speed information from the cleaned dataset.

## 3. How can I run the dashboard?

Run `streamlit run dashboard/app.py` from the project root directory.

## 4. Where is the cleaned dataset stored?

The expected path is `r"C:\Users\rohit\OneDrive\Desktop\atmosync project\processed\atmosync_microclimate_cleaned.csv"`.

## 5. Why is the dashboard showing a dataset error?

Check that the cleaned CSV exists at the expected path and contains the required columns.

## 6. How do I filter locations?

Use the location selection control to select the locations you want to explore.

## 7. What should I do if charts are empty?

Check the selected locations, dataset values, and date format.

## 8. Does the dashboard predict future weather?

The current dashboard summarizes recorded data. Forecasting is not included unless implemented separately.
