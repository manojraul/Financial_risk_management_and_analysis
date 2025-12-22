# Financial Risk Management and Analysis System

## Overview
This project analyzes the financial risk and return of selected stocks using Python. It applies **K-Means clustering** to categorize stocks into different risk levels based on **annualized return** and **volatility**. The system also calculates the **Sharpe ratio** and visualizes the clusters for easier interpretation.

## Features
- Fetches historical stock data from Yahoo Finance.
- Calculates daily returns, annualized returns, and volatility.
- Computes Sharpe ratio for risk-adjusted performance.
- Applies K-Means clustering to classify stocks into **Low, Medium, and High Risk**.
- Visualizes clusters using Matplotlib.
- Saves analysis results as CSV files.
- Generates a correlation matrix of the selected stocks.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- scikit-learn (K-Means)
- yfinance

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/manojraul/Financial_risk_management_and_analysis.git
