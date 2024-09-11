import yfinance as yf
import pandas as pd
from datetime import datetime

# Ensure openpyxl is installed for Excel operations
try:
    import openpyxl
except ImportError:
    print("The 'openpyxl' library is not installed. Please install it using 'pip install openpyxl'.")
    exit(1)

# Function to fetch OHLC data
def fetch_ohlc_data(ticker_symbol, start_date, end_date):
    data = yf.download(ticker_symbol, start=start_date, end=end_date, interval="1d")
    return data

# Function to save data to Excel
def save_to_excel(data, filename):
    data.to_excel(filename, sheet_name='OHLC Data')
    print(f"Data saved to {filename}")

def main():
    ticker_symbol = "TBZ.NS"
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    try:
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')

        data = fetch_ohlc_data(ticker_symbol, start_date, end_date)
        print("OHLC Data for TBZ Jewellers:")
        print(data)
        
        filename = "tbz_ohlc_data.xlsx"
        save_to_excel(data, filename)

    except ValueError as e:
        print(f"Error: {e}. Please enter the date in YYYY-MM-DD format.")

if __name__ == "__main__":
    main()
