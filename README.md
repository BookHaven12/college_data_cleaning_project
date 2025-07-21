# College Student Data Cleaning Project

## Overview

This project demonstrates a complete data cleaning and validation pipeline using a synthetic dataset of college students. The dataset was programmatically generated to reflect common real-world data issues, such as missing values, inconsistent categorical entries, and temporal logic errors. The project simulates a scenario often encountered in institutional research or education analytics.

## Features

- Identifies and resolves data integrity issues (e.g., graduation before enrollment)
- Standardizes inconsistent values in categorical columns such as `gender` and `major`
- Handles missing and outlier values, including negative credits and GPA values over 4.0
- Classifies students by graduation status (`Graduated` or `In Progress`)
- Estimates missing graduation years using a rule-based approach (enrollment year + 4)
- Formats date and year columns for clean, professional output

## Tools Used

- Python 3
- Pandas
- NumPy
- Jupyter Notebook

## Resources

The dataset used in this project was synthetically generated using Python and does not contain any real student information. It was designed to simulate realistic data integrity issues for educational and portfolio purposes. 


