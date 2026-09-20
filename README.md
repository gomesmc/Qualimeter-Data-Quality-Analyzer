# Qualímetro — Data Quality Report 

Qualímetro is a Streamlit-based application designed to help users inspect, understand, and evaluate the quality of datasets through a simple and intuitive interface.

The application allows users to upload datasets, preview their structure, inspect basic metadata, and serves as the foundation for generating automated data quality diagnostics and reports.

---

## Overview

Data quality is an important step before performing analysis, building dashboards, or training machine learning models.

Qualímetro aims to simplify this process by providing a visual interface where users can upload a dataset and quickly understand its structure before performing deeper quality checks.

The project is being developed incrementally, starting with file upload and dataset inspection and evolving toward automated data quality analysis.

---

## Current Features

The current version includes:

- Upload datasets through a Streamlit interface
- Support for:
  - CSV
  - Excel (`.xlsx`)
  - JSON
- Automatic file type detection
- Dataset loading with Pandas
- Dataset preview
- Display of:
  - Number of rows
  - Number of columns
  - Memory usage
  - Column names
  - Data types
- File information:
  - File name
  - File format
  - File size
- Custom application styling
- Responsive interface using Streamlit native components

---

## Planned Features

The project is currently under development.

Future versions are expected to include:

- Missing values analysis
- Duplicate record detection
- Empty string detection
- Data type validation
- Outlier detection
- Data consistency checks
- Data completeness indicators
- Data quality metrics
- Visual diagnostics
- Automated data quality score
- Automated quality report generation

---

## Technologies

The project currently uses:

- Python
- Streamlit
- Pandas
- CSS

Additional libraries may be introduced as the data quality analysis features evolve.

---

## Project Structure

```text
quality_report_data/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── src/
    └── styles/
        └── style.css