import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

# Step 1: Define the function to fetch OHLC data from Yahoo Finance
def fetch_ohlc_data(ticker_symbol, start_date, end_date):
    # Fetch data from Yahoo Finance
    data = yf.download(ticker_symbol, start=start_date, end=end_date, interval="1d")
    return data

# Step 2: Define the function to save data to a SQLite database
def save_to_database(data, db_name, table_name):
    # Create a connection to SQLite database (if it doesn't exist, it will be created)
    engine = create_engine(f'sqlite:///{db_name}.db', echo=False)

    # Store data in the specified table
    data.to_sql(table_name, con=engine, if_exists='replace', index=True)
    print(f"Data saved to {db_name}.db in table '{table_name}'")

def main():
    # Set the ticker symbol and date range
    ticker_symbol = "TBZ.NS"  # Replace with the correct ticker symbol
    start_date = "2023-01-01"  # Start date (1 year ago)
    end_date = "2023-12-31"    # End date

    # Fetch OHLC data
    data = fetch_ohlc_data(ticker_symbol, start_date, end_date)
    
    if not data.empty:
        # Define database name and table name
        db_name = "stock_data"
        table_name = "tbz_ohlc_data"

        # Save the data to the database
        save_to_database(data, db_name, table_name)
    else:
        print("No data fetched. Please check the ticker symbol and date range.")

if __name__ == "__main__":
    main()
