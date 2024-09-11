import requests
import pandas as pd

# Replace with your actual access token
ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzI4NDg1MTYzLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMzU5OTY3MCJ9.q7bbzSc5jMi16mQBdWSFmVHVXZlYoVTWDTedsvnnRsBkk7XgjLB7_vRIgmeSB5pI7QTZnNWps1lQ064GyzpX"  # Replace with your actual access token

# Base URL for DHAN API
BASE_URL = "https://api.dhan.co/holdings"

# Function to fetch holdings data from DHAN API
def fetch_holdings():
    url = BASE_URL  # Endpoint for fetching holdings (adjust if different)
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Accept': 'application/json'
}
      
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code} - {response.text}")
        return None

# Function to save data to Excel
def save_to_excel(data, filename):
    # Convert the data into a DataFrame
    df = pd.DataFrame(data['holdings'])  # Adjust 'holdings' based on actual response structure
    df.to_excel(filename, index=False, sheet_name='Holdings')
    print(f"Data saved to {filename}")

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
