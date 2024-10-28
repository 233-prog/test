from datetime import datetime
import pandas as pd

# Sample trades dictionary
# Each trade entry contains: symbol, buying date, selling date, quantity, and buy price
trades = [
    {"symbol": "AAPL", "buying_date": "2024-02-01", "selling_date": "2024-06-01", "quantity": 10, "price": 150},
    {"symbol": "TSLA", "buying_date": "2024-03-01", "selling_date": "2024-05-15", "quantity": 5, "price": 200},
]

# Sample LTP data as a dictionary (Date, Symbol) : LTP price
ltp_data = {
    ("2024-02-01", "AAPL"): 152,
    ("2024-03-01", "TSLA"): 210,
    ("2024-04-01", "AAPL"): 160,
    ("2024-04-15", "TSLA"): 215,
    # Add more dates and LTP values as needed
}

# Function to get the LTP for a given date and symbol
def get_ltp(date, symbol):
    return ltp_data.get((date, symbol), 0)  # Returns 0 if LTP data is not found

# Initialize list to store results
results = []

# Current date for calculation
current_date = datetime.now().date()

# Iterate over each trade and perform calculations based on date conditions
for trade in trades:
    symbol = trade["symbol"]
    buying_date = datetime.strptime(trade["buying_date"], "%Y-%m-%d").date()
    selling_date = datetime.strptime(trade["selling_date"], "%Y-%m-%d").date()
    quantity = trade["quantity"]
    buy_price = trade["price"]
    
    # Determine if we need to calculate profit or loss based on date conditions
    if current_date < selling_date:
        if current_date >= buying_date:
            # Get LTP for the current date and calculate profit or loss
            ltp = get_ltp(current_date.strftime("%Y-%m-%d"), symbol)
            profit_loss = (ltp - buy_price) * quantity
        else:
            profit_loss = 0
    else:
        profit_loss = 0
    
    # Append the result for each trade
    results.append({
        "symbol": symbol,
        "profit_loss": profit_loss,
    })

# Convert results to a DataFrame and print
df = pd.DataFrame(results)
print(df)

