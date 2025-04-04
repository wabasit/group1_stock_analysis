# Stock Price Analysis Project

A collaborative project to analyze historical stock prices by building a complete data pipeline — from data collection to visualization and testing.

---

## Project Overview

This project involves:
- Collecting stock data
- Cleaning the data
- Performing statistical operations like moving averages
- Analyzing correlations between different stocks
- Visualizing trends and relationships
- Ensuring correctness and reliability using unit tests

---

## Data Sources

- **Kaggle Stock Data Price
  
## Data Pipeline Workflow

### 1. Data Collection
- Download stock price data from kaggle.
- Collected data includes Open, High, Low, Close, Adj Close, and Volume.

### 2. Data Cleaning
- Removes:
  - Rows with missing (`NaN`) values
  - Duplicate records
- Converts date columns to `datetime` format

### 3. Feature Engineering
- Calculates:
  - Moving averages (e.g., 5-day, 20-day)

### 4. Correlation Analysis
- Computes Pearson correlation between the daily returns of different stocks
- Helps understand how stocks move in relation to each other

### 5. Data Visualization
- Line plots of closing prices and moving averages
- Correlation heatmap of returns
- Trend comparisons across stocks

---

## Unit Testing

We use `unittest` to verify:
- Data cleaning logic like removal of NaNs and duplicates
- Moving average calculations
- Edge case handling

Run tests using:

```bash
python -m unittest discover tests


