Sales Data Cleaning & Revenue Analysis
This project focuses on cleaning and analyzing a messy sales dataset using Python and pandas.
The goal is to transform inconsistent raw data into structured, analyzable information and extract meaningful business insights.
Project Files
cleaningandanalyze.py → Data cleaning and analysis script
dirtysales.csv → Original raw dataset
Data Cleaning Process
The dataset contained multiple formatting and consistency issues. The following steps were applied:
Removed currency symbols and cleaned unit price values
Standardized numeric columns (price, quantity, discount)
Converted data types properly (string → numeric)
Detected and handled unrealistic discount values
Applied IQR method to identify outliers
Created a new calculated column: net_revenue
Analysis Performed
After cleaning, the following insights were generated:
Total net revenue
Average revenue per transaction
Revenue comparison between discounted and non-discounted sales
Top 5 highest revenue generating products
Descriptive statistics of revenue distribution
Technologies Used
Python
pandas
Purpose
This project demonstrates practical data cleaning, transformation, and basic business analysis skills using real-world messy data.
