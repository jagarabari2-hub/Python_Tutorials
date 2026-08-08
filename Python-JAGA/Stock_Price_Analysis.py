# Stock Price Analysis

# Download historical stock data and analyse it with Pandas time series tools.

# In this project, you will download historical stock price data and analyze it using Pandas time series tools. You will work with dates as an index, resample data at different frequencies, and compute moving averages.

# Stock data is a natural fit for time series because it changes every day and has a clear structure: open, close, high, low, volume.
# Project Requirements

#     Download historical stock data for at least two companies using the yfinance library

#     Set the date column as the DataFrame index

#     Plot closing prices over time using line charts

#     Resample data to weekly and monthly frequency using .resample()

#     Compute 20-day and 200-day moving averages with .rolling()

#     Compare trading volume between the two companies

# Technologies to Use

#     Python

#     Pandas

#     yfinance

#     Matplotlib

#     Jupyter Notebook
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
# Download historical stock data for two companies
tickers = ['AAPL', 'GOOGL']
data = {}

for ticker in tickers:
    data[ticker] = yf.download(ticker, start='2023-01-01', end='2024-01-01')

# Set the date as index (already done by yfinance)
# Plot closing prices
plt.figure(figsize=(12, 6))
for ticker in tickers:
    plt.plot(data[ticker].index, data[ticker]['Close'], label=ticker)
plt.title('Stock Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.show()