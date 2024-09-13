import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Input JSON data
input_json = [
    {"Symbol": "INDUSTOWER", "Min": 425, "Max": 450},
    {"Symbol": "IREDA", "Min": 200, "Max": 250},
    {"Symbol": "RVNL", "Min": 500, "Max": 575},
    {"Symbol": "SUZLON", "Min": 45, "Max": 60},
    {"Symbol": "COCHINSHIP", "Min": 1750, "Max": 2200}
]

# Define the date range
end_date = datetime.now()
start_date = end_date - timedelta(days=90)

# Create a DataFrame to store results
results = []

for item in input_json:
    symbol = item["Symbol"] + ".NS"  # Append ".NS" to the symbol
    min_price = item["Min"]
    max_price = item["Max"]
    
    # Fetch stock data
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    
    # Extract the closing prices
    stock_data['Date'] = stock_data.index
    stock_data = stock_data[['Date', 'Close']]
    
    # Add high/low column based on the Min and Max values
    stock_data['High/Low'] = stock_data['Close'].apply(lambda x: 'High' if x > max_price else ('Low' if x < min_price else 'Normal'))
    
    # Filter out 'Normal' values
    stock_data = stock_data[stock_data['High/Low'] != 'Normal']
    
    # Add Symbol column and append to results
    stock_data['Symbol'] = item["Symbol"]
    results.append(stock_data)

# Combine all results into a single DataFrame
all_data = pd.concat(results)

# Reorder the columns
all_data = all_data[['Date', 'Symbol', 'Close', 'High/Low']]

# Save to Excel file
output_file = 'filtered_stock_data.xlsx'
all_data.to_excel(output_file, index=False)

print(f'Data has been written to {output_file}')

# Print stock names vertically only if they are marked as High or Low
print("Stocks with High or Low Closing Prices:")
for symbol in all_data['Symbol'].unique():
    print(symbol)
