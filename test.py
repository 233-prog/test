import requests
import pandas as pd
import yfinance as yf
from datetime import datetime

ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzI4NDg1MTYzLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMzU5OTY3MCJ9.q7bbzSc5jMi16mQBdWSFmVHVXZlYoVTWDTedsvnnRsBkk7XgjLB7_vRIgmeSB5pI7QTZnNWps1lQ064GyzpX-w"

# Function to fetch portfolio holdings from Dhan API
def fetch_dhan_holdings(api_key):
    url = "https://api.dhan.co/holdings"  # Replace with the correct endpoint from Dhan API docs
    headers = {
        "access-token": ACCESS_TOKEN,
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        holdings = response.json()

        # Check if the response is a valid list of holdings
        if not isinstance(holdings, list) or not holdings:
            print("No holdings data found or invalid format received.")
            return []
        
        return holdings
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    
    return []

# Function to fetch daily stock data using yfinance
def fetch_latest_stock_prices(tickers):
    stock_data = {}
    for ticker in tickers:
        stock_info = yf.download(ticker, period="1d")  # Fetch today's data
        if not stock_info.empty:
            stock_data[ticker] = stock_info.iloc[-1]  # Get the latest row
    return stock_data

# Function to create a portfolio tracking Excel file
def create_portfolio_excel(holdings, stock_data):
    portfolio = []

    for holding in holdings:
        # Ensure that the holding contains the required keys
        if 'symbol' not in holding or 'quantity' not in holding or 'buy_price' not in holding:
            print(f"Invalid holding format: {holding}")
            continue

        ticker = holding['symbol']
        quantity = holding['quantity']
        avg_cost = holding['buy_price']
        today = datetime.now().strftime('%Y-%m-%d')

        # Fetch today's stock data
        if ticker in stock_data:
            ltp = stock_data[ticker]['Close']
            cur_val = quantity * ltp
            pnl = (ltp - avg_cost) * quantity
            net_chg = ltp - avg_cost
            day_chg = stock_data[ticker]['Close'] - stock_data[ticker]['Open']

            portfolio.append({
                'Instrument': ticker,
                'Qty.': quantity,
                'Avg. cost': avg_cost,
                'LTP': ltp,
                'Cur. val': cur_val,
                'P&L': pnl,
                'Net chg.': net_chg,
                'Day chg.': day_chg
            })

    # Create a DataFrame and save to Excel
    df = pd.DataFrame(portfolio)
    file_name = f"Portfolio_Summary_{today}.xlsx"
    df.to_excel(file_name, index=False)
    print(f"Portfolio data saved to {file_name}")

# Main function to execute the program
def main():
    # Replace with your Dhan API key
    api_key = "yeyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzI4NDg1MTYzLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMzU5OTY3MCJ9.q7bbzSc5jMi16mQBdWSFmVHVXZlYoVTWDTedsvnnRsBkk7XgjLB7_vRIgmeSB5pI7QTZnNWps1lQ064GyzpX-wour_dhan_api_key"

    # Fetch portfolio holdings from Dhan
    holdings = fetch_dhan_holdings(api_key)

    if not holdings:
        print("No holdings data available.")
        return

    # Extract tickers from holdings
    try:
        tickers = [holding['symbol'] for holding in holdings if 'symbol' in holding]
    except KeyError as e:
        print(f"KeyError: {e} in holdings data.")
        return

    # Fetch daily stock data using yfinance
    stock_data = fetch_latest_stock_prices(tickers)

    # Create the Excel file for portfolio tracking
    create_portfolio_excel(holdings, stock_data)

if __name__ == "__main__":
    main()
