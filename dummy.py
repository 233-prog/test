import requests
import pandas as pd
import yfinance as yf
from datetime import datetime

ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzI4NDg1MTYzLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMzU5OTY3MCJ9.q7bbzSc5jMi16mQBdWSFmVHVXZlYoVTWDTedsvnnRsBkk7XgjLB7_vRIgmeSB5pI7QTZnNWps1lQ064GyzpX-w"

# Function to fetch portfolio holdings from Dhan API
def fetch_dhan_holdings(api_key):
    url = "https://api.dhan.co/holdings"  # Adjust endpoint as necessary
    headers = {"access-token": ACCESS_TOKEN,}
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []

# Function to extract symbols from holdings
def extract_symbols(holdings):
    symbols = {holding['tradingSymbol'+".NS"] for holding in holdings if 'tradingSymbol'+".NS" in holding}
    return list(symbols)

# Function to fetch daily stock data using yfinance
def fetch_stock_data(tickers):
    stock_data = {}
    for ticker in tickers:
        data = yf.download(ticker, period="1d")
        if not data.empty:
            stock_data[ticker] = data['Close'].iloc[-1]  # Closing price for today
    return stock_data

# Function to create an Excel file for portfolio holdings
def create_portfolio_excel(holdings, stock_data):
    portfolio = []
    for holding in holdings:
        symbol = holding.get('tradingSymbol')
        quantity = holding.get('totalQty', 0)
        avg_cost = holding.get('avgCostPrice', 0)
        current_price = stock_data.get(symbol, 0)
        total_value = quantity * current_price
        day_change = current_price - avg_cost

        portfolio.append({
            'Instrument': symbol,
            'Quantity': quantity,
            'Avg. Cost': avg_cost,
            'LTP': current_price,
            'Cur. Val': total_value,
            'P&L': total_value - (quantity * avg_cost),
            'Net Chg.': day_change,
            'Day Chg.': current_price - avg_cost
        })

    df = pd.DataFrame(portfolio)
    file_name = f"Portfolio_Holdings_{datetime.now().strftime('%Y-%m-%d')}.xlsx"
    df.to_excel(file_name, index=False)
    print(f"Portfolio data saved to {file_name}")

# Main function to execute the program
def main():
    # Replace with your Dhan API key
    api_key = "yeyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzI4NDg1MTYzLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMzU5OTY3MCJ9.q7bbzSc5jMi16mQBdWSFmVHVXZlYoVTWDTedsvnnRsBkk7XgjLB7_vRIgmeSB5pI7QTZnNWps1lQ064GyzpX-w"

    # Fetch portfolio holdings from Dhan
    holdings = fetch_dhan_holdings(api_key)
    if not holdings:
        print("No holdings data available.")
        return

    # Extract symbols and fetch stock data
    symbols = extract_symbols(holdings)
    stock_data = fetch_stock_data(symbols)

    # Create the Excel file for portfolio holdings
    create_portfolio_excel(holdings, stock_data)

if __name__ == "__main__":
    main()
