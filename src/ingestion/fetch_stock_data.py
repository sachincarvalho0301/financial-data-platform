import yfinance as yf
import pandas as pd

# Define stock ticker
ticker = "RELIANCE.NS"

# Download historical stock data
df = yf.download(
    ticker,
    start="2025-01-01",
    end="2026-01-01"
)

# Reset index
df.reset_index(inplace=True)

# Save raw data
df.to_csv("data/reliance_stock_data.csv", index=False)

print("Stock data extracted successfully!")
print(df.head())