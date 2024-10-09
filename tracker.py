import yfinance as yf
import pandas as pd

# 1. Fetching the purchase details from the Dhan API (Placeholder code)
# This part will depend on how the API is called. Let's assume you have a function like this:
def get_purchase_details():
    # Replace with your API call to get the stock symbol, purchase date, purchase price, and quantity
    purchase_info = {
        'symbol': 'TBZ.NS',  # Example stock symbol for TCS
        'purchase_date': '2024-08-12',  # Example purchase date
        'purchase_price': 164.4,  # Example purchase price
        'quantity': 30  # Number of stocks purchased
    }
    return purchase_info

# 2. Get the purchase details
purchase_details = get_purchase_details()
symbol = purchase_details['symbol']
purchase_date = purchase_details['purchase_date']
purchase_price = purchase_details['purchase_price']
quantity = purchase_details['quantity']

# 3. Fetch historical data from yfinance for the stock
stock_data = yf.download(symbol, start=purchase_date)

# 4. Add a new column 'My Value' to the DataFrame by multiplying the 'Close' price with the quantity
stock_data['My Value'] = stock_data['Close'] * quantity

# 5. Calculate profit or loss for each day
initial_investment = purchase_price * quantity
stock_data['Profit/Loss'] = stock_data['My Value'] - initial_investment

# 6. Display the data
print(stock_data[['Close', 'My Value', 'Profit/Loss']])

# Optionally save to an Excel file or CSV
stock_data[['Close', 'My Value', 'Profit/Loss']].to_csv(f'{symbol}_stock_value.csv')

