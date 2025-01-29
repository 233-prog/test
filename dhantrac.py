import requests
import pandas as pd
from datetime import datetime

# Function to fetch the trade and ledger details from the Dhan API
def fetch_trade_and_ledger_data():
    # Set up your API credentials and endpoint
    api_url = "https://api.dhan.co/v1/portfolio"  # Placeholder - change it to the correct endpoint
    api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzQwNjUwNTE4LCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMzU5OTY3MCJ9.fghPDIJj-Yfo3vaa6rUf4upOcK36WPhqBoOlzDb3BK1UqayfUOxsDmjr7506J7pHZaCURqIOYfURSUG0SkyNHA"  # Replace with your actual API key

    # Set up the headers and parameters for the request
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    # Set the fixed start date to 1st June 2024
    start_date = datetime(2024, 6, 1)
    end_date = datetime.today()

    # Convert dates to string format
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    params = {
        "start_date": start_date_str,
        "end_date": end_date_str,
    }

    # Send a GET request to the API
    response = requests.get(api_url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        # Print detailed error message if the request fails
        print(f"Error fetching data: {response.status_code}")
        print("Response Content:", response.text)  # This will show more details about the error
        return None

# Function to process the trade and ledger data and save it to Excel
def process_and_save_data(data):
    # Convert the raw API response into a DataFrame
    df = pd.DataFrame(data['transactions'])  # Adjust 'transactions' based on the API response structure

    # Calculate the daily P&L
    df['date'] = pd.to_datetime(df['date'])
    df['profit_loss'] = df['amount']  # Adjust 'amount' field to represent P&L

    # Group the data by date and calculate total P&L for each day
    daily_pnl = df.groupby(df['date'].dt.date)['profit_loss'].sum().reset_index()
    
    # Save the report to an Excel file
    output_filename = "daily_profit_loss_report.xlsx"
    daily_pnl.to_excel(output_filename, index=False)

    print(f"Report saved as {output_filename}")

# Main function to execute the program
def main():
    # Fetch the trade and ledger data from the Dhan API
    data = fetch_trade_and_ledger_data()

    if data:
        # Process the data and save it to Excel
        process_and_save_data(data)

if __name__ == "__main__":
    main()
