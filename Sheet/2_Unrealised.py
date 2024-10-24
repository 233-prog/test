import yfinance as yf
import pandas as pd
import requests


DHAN_API_URL = "https://api.dhan.co/" 
API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzMyMjY1OTQzLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMzU5OTY3MCJ9.RDv1yTGL_vMnfmx2s5Z1SdGo6SBCbNs9LMhV0krqp2K5ndMlk_l75XMRRoMWr89-DRAqfVKnzG648Mfl2d8_TQ"

# Fetch stock data from Yahoo Finance
def fetch_stock_data(symbol, start_date='2024-02-01'):
    stock = yf.Ticker(symbol + '.NS')
    data = stock.history(start=start_date)
    return data

# Fetch holdings from Dhan API
def get_holdings():
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(f"{DHAN_API_URL}/holdings", headers=headers)
    if response.status_code == 200:
        holdings = response.json()
        return holdings['data']
    else:
        print(f"Failed to fetch holdings: {response.status_code}")
        return None

# Calculate profit or loss for a single holding
def calculate_profit_loss(stock_data, holding):
    symbol = holding['symbol']
    quantity = holding['quantity']
    buy_price = holding['buy_price']
    latest_price = stock_data['Close'].iloc[-1]
    profit_loss = (latest_price - buy_price) * quantity
    return profit_loss

# Calculate profit or loss for all holdings
def calculate_all_profits(holdings):
    results = []
    for holding in holdings:
        symbol = holding['symbol']
        stock_data = fetch_stock_data(symbol)
        if stock_data is not None and not stock_data.empty:
            profit_loss = calculate_profit_loss(stock_data, holding)
            results.append({'symbol': symbol, 'profit_loss': profit_loss})
    return results

# Save results to Excel
def save_to_excel(data, filename="profit_loss_report.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

# Main execution
holdings = get_holdings()
if holdings:
    profits = calculate_all_profits(holdings)
    save_to_excel(profits)
