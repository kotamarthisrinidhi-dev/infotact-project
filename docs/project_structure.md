# AtmoSync Project Structure

## Project Overview

The AtmoSync project is organized into separate folders for dataset management, analysis, dashboard development, and documentation.

## Main Folders

### dataset/

Contains the project datasets.

#### dataset/raw/

Stores the original AtmoSync micro-climate dataset.

Example:

- atmosync_microclimate_raw.csv

#### dataset/processed/

Stores cleaned and processed datasets generated during data preparation.

---

### analysis/

Contains Python scripts used for:

- Data loading
- Data inspection
- Data cleaning
- Exploratory data analysis
- Weather analysis
- Correlation analysis
- Visualizations

---

### dashboard/

Contains the Streamlit dashboard application and related dashboard components.

---

### docs/

Contains project documentation such as:

- Project overview
- Project objectives
- Dataset description
- Data dictionary
- Analysis plan
- Analysis workflow
- Data validation
- Setup guide

---

## Root Files

### README.md

Contains the main project introduction and overview.

### requirements.txt

Contains the Python libraries required for the AtmoSync project.

### .gitignore

Contains files and folders that should not be committed to GitHub.

## Project Structure

text
AtmoSync/
├── dataset/
│   ├── raw/
│   └── processed/
├── analysis/
├── dashboard/
├── docs/
├── README.md
├── requirements.txt
└── .gitignore
`
