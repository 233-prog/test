import pandas as pd

# Example Trades
trades = [
    {'date': '2023-01-01', 'script': 'SUZLON', 'type': 'Buy', 'qty': 10, 'price': 20, 'amt': -200},
    {'date': '2023-01-02', 'script': 'TBZ', 'type': 'Buy', 'qty': 20, 'price': 30, 'amt': -600},
    {'date': '2023-01-03', 'script': 'TBZ', 'type': 'Sell', 'qty': -20, 'price': 40, 'amt': 800}
]

# Convert the trades to a DataFrame
df = pd.DataFrame(trades)

# Initialize a column for 'pair_number' to track matched Buy and Sell transactions
df['pair_number'] = None

# Create a unique pair number
pair_number = 1

# Function to process Buy and Sell pairs
def process_trades(df):
    global pair_number

    # Create a DataFrame for Buy orders and one for Sell orders
    buys = df[df['type'] == 'Buy'].copy()
    sells = df[df['type'] == 'Sell'].copy()

    # Loop through each sell order
    for i, sell in sells.iterrows():
        script = sell['script']
        sell_qty = abs(sell['qty'])  # Convert to positive for quantity matching

        # Find matching buys for the same script, using FIFO (by date order)
        matching_buys = buys[(buys['script'] == script) & (buys['qty'] > 0)].sort_values('date')

        # Process each matching buy until the sell order is fully paired
        for j, buy in matching_buys.iterrows():
            buy_qty = buy['qty']

            # Full match: Sell matches completely with one buy
            if buy_qty >= sell_qty:
                # Assign the same pair number to both the sell and the matched buy
                df.at[i, 'pair_number'] = pair_number
                df.at[buy.name, 'pair_number'] = pair_number

                # Reduce the quantity of the buy by the sold quantity
                df.at[buy.name, 'qty'] = buy_qty - sell_qty

                # Increment the pair number for next pairing
                pair_number += 1

                # Break once the sell is fully matched
                break

            # Partial match: Buy quantity is smaller than sell quantity
            elif buy_qty < sell_qty:
                # Assign the same pair number to both the sell and the matched buy
                df.at[i, 'pair_number'] = pair_number
                df.at[buy.name, 'pair_number'] = pair_number

                # Reduce the sell quantity by the amount of the current buy
                sell_qty -= buy_qty

                # Set the buy quantity to 0 as it's fully paired
                df.at[buy.name, 'qty'] = 0

                # Increment the pair number for the next match
                pair_number += 1

    return df

# Process the trades and match buy and sell orders
df_processed = process_trades(df)

# Display the updated DataFrame with paired trades
print(df_processed)
