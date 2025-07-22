# College Student Data Cleaning Project

## Overview

This project showcases a full data cleaning and validation process using a synthetic college student dataset. It reflects common real-world issues like inconsistent labels, missing values, logic errors, and outliers. The cleaning workflow uses Python, Pandas, and NumPy to standardize categories, fix date inconsistencies, engineer new features, and organize output files in a reproducible way. The result is a well-structured dataset that’s ready for analysis and reporting.

## Features

- Detects and resolves data integrity issues such as graduation dates preceding enrollment
- Standardizes inconsistent categorical values, including variations in gender and major
- Identifies and corrects missing values and outliers, such as negative credit hours or GPAs exceeding 4.0
- Classifies students based on graduation status (e.g., Graduated or In Progress)
- Estimates missing graduation years using a transparent, rule-based method (enrollment year + 4)
- Ensures consistent formatting for date and year fields to support clean analysis and reporting

## Tools Used

- Python 3
- Pandas
- NumPy
- Jupyter Notebook

## Resources

The dataset used in this project was synthetically generated using Python and does not contain any real student information. It was designed to simulate realistic data integrity issues for educational and portfolio purposes. 