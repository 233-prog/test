import requests
import pandas as pd

# Replace with your actual access token securely
ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzI4NDg1MTYzLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMzU5OTY3MCJ9.q7bbzSc5jMi16mQBdWSFmVHVXZlYoVTWDTedsvnnRsBkk7XgjLB7_vRIgmeSB5pI7QTZnNWps1lQ064GyzpX"

# Base URL for DHAN API (check if this is the correct endpoint)
BASE_URL = "https://api.dhan.co/trades/api/v1/holdings"

# Function to fetch holdings data from DHAN API
def fetch_holdings():
    url = BASE_URL  # Endpoint for fetching holdings (adjust if different)
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - {response.text}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    
    return None

# Function to save data to Excel
def save_to_excel(data, filename):
    try:
        # Convert the data into a DataFrame
        df = pd.DataFrame(data['holdings'])  # Adjust 'holdings' based on actual response structure
        df.to_excel(filename, index=False, sheet_name='Holdings')
        print(f"Data saved to {filename}")
    except KeyError:
        print("Error: The response data does not have the expected 'holdings' key.")
    except Exception as e:
        print(f"An error occurred while saving to Excel: {e}")

def main():
    # Fetch holdings data
    holdings_data = fetch_holdings()
    
    if holdings_data:
        # Print data for verification
        print("Holdings Data:")
        print(holdings_data)
        
        # Save data to Excel
        filename = "dhan_holdings.xlsx"
        save_to_excel(holdings_data, filename)

if __name__ == "__main__":
    main()
