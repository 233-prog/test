import requests

# Your Dhan API access token
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzI4NDg1MTYzLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMzU5OTY3MCJ9.q7bbzSc5jMi16mQBdWSFmVHVXZlYoVTWDTedsvnnRsBkk7XgjLB7_vRIgmeSB5pI7QTZnNWps1lQ064GyzpX-w"

# Set up the headers with your access token
headers = {
    'access-token': access_token,
    'Accept': 'application/json'
}

# Define the API endpoint for fetching holdings
api_url = "https://dhan.co"

try:
    # Make a GET request to fetch holdings data
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data returned by the API
        holdings_data = response.json()

        # Check if the response is a list
        if isinstance(holdings_data, list):
            print("Your Current Holdings in Dhan:")
            print("===================================")
            for holding in holdings_data:
                stock_name = holding.get('symbol')
                quantity = holding.get('quantity')
                average_price = holding.get('averagePrice')
                current_price = holding.get('currentPrice')
                investment_value = holding.get('investmentValue')
                current_value = holding.get('currentValue')

                print(f"Stock: {stock_name}")
                print(f"Quantity: {quantity}")
                print(f"Average Price: {average_price}")
                print(f"Current Price: {current_price}")
                print(f"Investment Value: {investment_value}")
                print(f"Current Value: {current_value}")
                print("-----------------------------------")
        else:
            print("Unexpected response format:", holdings_data)

    else:
        print(f"Failed to fetch holdings: {response.status_code} - {response.text}")

except Exception as e:
    print(f"An error occurred: {e}")
