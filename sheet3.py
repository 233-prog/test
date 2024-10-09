import pandas as pd

# Sample trades data
trades = [
    {'date': '2023-04-18', 'symbol': 'VOLTAS', 'type': 'BUY', 'qty': 39, 'price': 1311.00, 'amt': -51129.00},
    {'date': '2023-05-17', 'symbol': 'INDIANHUME', 'type': 'BUY', 'qty': 800, 'price': 323.96, 'amt': -259170.00},
    {'date': '2023-05-24', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'BUY', 'qty': 1000, 'price': 799.98, 'amt': -799980.00},
    {'date': '2023-05-27', 'symbol': 'VOLTAS', 'type': 'BUY', 'qty': 211, 'price': 1424.88, 'amt': -300650.00},
    {'date': '2023-06-13', 'symbol': 'VOLTAS', 'type': 'SELL', 'qty': -39, 'price': 1480.55, 'amt': 57741.00},
    {'date': '2023-06-13', 'symbol': 'VOLTAS', 'type': 'SELL', 'qty': -211, 'price': 1480.55, 'amt': 312396.00},
    {'date': '2023-06-13', 'symbol': 'GULPOLY', 'type': 'BUY', 'qty': 1500, 'price': 214.20, 'amt': -321300.00},
    {'date': '2023-07-11', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'BUY', 'qty': 1000, 'price': 927.50, 'amt': -927500.00},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -201, 'price': 900.00, 'amt': 180900.00},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -5, 'price': 899.80, 'amt': 4499.00},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -92, 'price': 899.70, 'amt': 82772.40},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -4, 'price': 899.65, 'amt': 3598.60},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -351, 'price': 899.60, 'amt': 315759.60},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -4, 'price': 899.55, 'amt': 3598.20},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -11, 'price': 899.50, 'amt': 9894.50},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -8, 'price': 899.45, 'amt': 7195.60},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -69, 'price': 899.40, 'amt': 62058.60},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -30, 'price': 899.35, 'amt': 26980.50},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -55, 'price': 899.30, 'amt': 49461.50},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -8, 'price': 899.25, 'amt': 7194.00},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -16, 'price': 899.20, 'amt': 14387.20},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -18, 'price': 899.15, 'amt': 16184.70},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -12, 'price': 899.10, 'amt': 10789.20},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -116, 'price': 899.05, 'amt': 104289.80},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -38, 'price': 899.05, 'amt': 34163.90},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -149, 'price': 899.00, 'amt': 133951.00},
    {'date': '2023-07-22', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -813, 'price': 904.00, 'amt': 734952.00},
    {'date': '2023-08-06', 'symbol': 'SHAKTIPUMP', 'type': 'BUY', 'qty': 350, 'price': 4785.66, 'amt': -1674981.00}
]

# Convert trades data into a DataFrame
df = pd.DataFrame(trades)

# Initialize a column for 'pair_number' to track matched Buy and Sell transactions
df['pair_number'] = None

# Create a unique pair number
pair_number = 1

# Function to process Buy and Sell pairs
def process_trades(df):
    global pair_number

    # Create a DataFrame for Buy orders and one for Sell orders
    buys = df[df['type'] == 'BUY'].copy()
    sells = df[df['type'] == 'SELL'].copy()

    # Loop through each sell order
    for i, sell in sells.iterrows():
        symbol = sell['symbol']
        sell_qty = abs(sell['qty'])  # Convert to positive for quantity matching

        # Find matching buys for the same symbol, using FIFO (by date order)
        matching_buys = buys[(buys['symbol'] == symbol) & (buys['qty'] > 0)].sort_values('date')

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

                # Increment the pair number for the next pairing
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

# Save the DataFrame to an Excel file
output_file = '/mnt/data/trades_pairing_multiple.xlsx'
df_processed.to_excel(output_file, index=False)

# Return the path to the generated file
output_file
