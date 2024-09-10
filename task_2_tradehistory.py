import requests
import json

# Define the access token (replace with actual token)
ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzI4NDg1MTYzLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMzU5OTY3MCJ9.q7bbzSc5jMi16mQBdWSFmVHVXZlYoVTWDTedsvnnRsBkk7XgjLB7_vRIgmeSB5pI7QTZnNWps1lQ064GyzpX-w"

# Set up headers for authentication
headers = {
    "access-token": ACCESS_TOKEN,
    "Accept": "application/json"
}

# Function to get trade history for a given date range
def get_trade_history(from_date, to_date, page=0):
    url = f"https://api.dhan.co/tradeHistory/{from_date}/{to_date}/{page}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching trade history: {response.status_code} - {response.text}")


json_data = get_trade_history("2024-08-01", "2024-08-30")

# print headers
print("Stock Name\tBuying Price\tQuantity\tDate Bought\tTransaction Type")

# Extract specific information
for trade in json_data:
    stock_name = trade['customSymbol']
    buying_price = trade['tradedPrice']
    quantity = trade['tradedQuantity']
    date_bought = trade['exchangeTime']
    transaction_type = trade['transactionType']

    print(f"{stock_name}\t{buying_price}\t{quantity}\t{date_bought}\t{transaction_type}")