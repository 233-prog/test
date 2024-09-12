import requests
import pandas as pd
import yfinance as yf
from datetime import datetime

ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzI4NDg1MTYzLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMzU5OTY3MCJ9.q7bbzSc5jMi16mQBdWSFmVHVXZlYoVTWDTedsvnnRsBkk7XgjLB7_vRIgmeSB5pI7QTZnNWps1lQ064GyzpX-w"

# Function to fetch portfolio holdings from Dhan API
def fetch_dhan_holdings(api_key):
    url = "https://api.dhan.co/holdings"  # Example endpoint, check Dhan API docs for the correct endpoint
    headers = {
        "access-token": ACCESS_TOKEN,
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        holdings = response.json()
        return holdings
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []

# Function to fetch daily stock data using yfinance
def fetch_daily_stock_data(tickers):
    stock_data = {}
    for ticker in tickers:
        stock_info = yf.download(ticker, period="1d")  # Fetch today's data
        if not stock_info.empty:
            stock_data[ticker] = stock_info
    return stock_data

# Function to create a portfolio tracking Excel file
def create_portfolio_excel(holdings, stock_data):
    portfolio = []

    for holding in holdings:
        ticker = holding['symbol']
        quantity = holding['quantity']
        buy_price = holding['buy_price']
        today = datetime.now().strftime('%Y-%m-%d')

        # Fetch today's stock data
        if ticker in stock_data:
            close_price = stock_data[ticker]['Close'].iloc[-1]
            day_change = close_price - buy_price
            total_value = quantity * close_price

            portfolio.append({
                'Date': today,
                'Stock': ticker,
                'Quantity': quantity,
                'Buy Price': buy_price,
                'Day End Price': close_price,
                'Daily Change in Price': day_change,
                'Total Value at Day End': total_value
            })

    # Create a DataFrame and save to Excel
    df = pd.DataFrame(portfolio)
    file_name = f"Portfolio_Tracking_{today}.xlsx"
    df.to_excel(file_name, index=False)
    print(f"Portfolio data saved to {file_name}")

# Main function to execute the program
def main():
    # Replace with your Dhan API credentials
    api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzI4NDg1MTYzLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMzU5OTY3MCJ9.q7bbzSc5jMi16mQBdWSFmVHVXZlYoVTWDTedsvnnRsBkk7XgjLB7_vRIgmeSB5pI7QTZnNWps1lQ064GyzpX-w"

    # Fetch portfolio holdings from Dhan
    holdings = fetch_dhan_holdings(api_key)

    if not holdings:
        print("No holdings data available.")
        return

    # Extract tickers from holdings
    tickers = [holding['symbol'] for holding in holdings]

    # Fetch daily stock data using yfinance
    stock_data = fetch_daily_stock_data(tickers)

    # Create the Excel file for portfolio tracking
    create_portfolio_excel(holdings, stock_data)

if __name__ == "__main__":
    main()
