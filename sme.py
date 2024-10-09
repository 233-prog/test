import yfinance as yf
import pandas as pd

# List of stock symbols (replace with actual symbols)
symbols = [
    'HEMHOL.BS',  # Add more actual symbols
    # ... continue for all stocks
]

# Create an empty DataFrame to store the closing prices
closing_prices = pd.DataFrame()

# Fetch the data for each stock symbol
for symbol in symbols:
    try:
        stock_data = yf.download(symbol, period='1m')  # Fetch 1 month of data as an example
        closing_prices[symbol] = stock_data['Close']  # Save only the closing price
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")

# Save the closing prices to an Excel file
closing_prices.to_excel('closing_prices.xlsx')

print("Closing prices saved to closing_prices.xlsx")
