import requests
import pandas as pd

# Dhan API details - You need to replace these with your actual API Key and Secret
API_KEY = 'yoeyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzI4NDg1MTYzLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMzU5OTY3MCJ9.q7bbzSc5jMi16mQBdWSFmVHVXZlYoVTWDTedsvnnRsBkk7XgjLB7_vRIgmeSB5pI7QTZnNWps1lQ064GyzpX-w'
BASE_URL = 'https://api.dhan.co/holdings'  # Example Dhan API base URL (replace if needed)

# Function to get the access token (OAuth2 or other mechanism)
def get_access_token():
    url = f'{BASE_URL}/oauth/token'  # Replace with the correct token endpoint
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'apiKey': API_KEY,
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        return response.json().get('access_token')  # Replace with the correct field
    else:
        raise Exception("Failed to get access token")

# Function to get BSE SME stock list and closing prices
def get_bse_sme_stocks(access_token):
    url = f'{BASE_URL}/markets/bse/sme_stocks'  # Replace with the correct Dhan API endpoint
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Assuming JSON format, adapt if necessary
    else:
        raise Exception("Failed to fetch BSE SME stocks")

# Main function to fetch stock data and save to Excel
def fetch_and_save_bse_sme_data():
    access_token = get_access_token()  # Get the access token
    
    # Fetch BSE SME stocks and their closing prices
    stock_data = get_bse_sme_stocks(access_token)
    
    # Process the stock data (this depends on the response format)
    stock_list = []
    
    # Assuming the response contains stock name, symbol, and closing price in JSON
    for stock in stock_data['stocks']:  # Adapt based on the actual JSON structure
        stock_list.append({
            'Stock Name': stock['name'],
            'Symbol': stock['symbol'],
            'Closing Price': stock['closingPrice']  # Replace with the actual field name
        })
    
    # Save the data to an Excel file
    df = pd.DataFrame(stock_list)
    df.to_excel('bse_sme_stocks.xlsx', index=False)
    
    print("Data saved to bse_sme_stocks.xlsx")

# Execute the function
if __name__ == "__main__":
    fetch_and_save_bse_sme_data()
