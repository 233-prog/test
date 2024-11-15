import pandas as pd
from datetime import datetime, timedelta
import yfinance as yf

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

# Add a 'pair' field to each trade, initialized as an empty string
for trade in trades:
    trade['pair'] = ''

# Pair counter to assign unique pair numbers
pair_number = 1

# Iterate over all trades to find SELL transactions and pair them with BUY transactions
for sell_trade in trades:
    if sell_trade['type'] == 'SELL':
        
        symbol = sell_trade['symbol']
        remaining_sell_qty = sell_trade['qty']
        pair_created = False

        # Loop through BUY trades for the same symbol to find a matching pair
        for buy_trade in trades:
            if (buy_trade['pair'] == '' and buy_trade['symbol'] == symbol and buy_trade['type'] == 'BUY'):
                buy_qty = buy_trade['qty']

                # If the sell quantity can be fully matched by the buy quantity
                if abs(buy_qty) <= abs(remaining_sell_qty):
                    remaining_sell_qty += buy_qty
                    buy_trade['pair'] = pair_number
                    sell_trade['pair'] = pair_number
                    pair_created = True

                else:
                    # Handle case where remaining sell quantity is less than buy quantity
                    if abs(remaining_sell_qty) > 0:
                        # Calculate new quantities and amounts after splitting the BUY trade
                        new_buy_qty = buy_qty + remaining_sell_qty
                        new_buy_amt = new_buy_qty * buy_trade['price'] * -1
                        new_buy_trade = buy_trade.copy()
                        new_buy_trade['qty'] = new_buy_qty
                        new_buy_trade['amt'] = new_buy_amt

                        # Update the original buy trade with remaining quantity
                        buy_trade['qty'] = abs(remaining_sell_qty)
                        buy_trade['amt'] = abs(remaining_sell_qty) * buy_trade['price'] * -1

                        # Append the newly created partial trade back to the trades list
                        trades.append(new_buy_trade)
                        trades = sorted(trades, key=lambda x: x['date'])

                        remaining_sell_qty = 0
                        buy_trade['pair'] = pair_number
                        sell_trade['pair'] = pair_number
                        pair_created = True

        if pair_created:
            pair_number += 1


# extract the symbol names
symbols = [row['symbol'] for row in trades if 'symbol' in row]
unique_symbols = list(set(symbols))

exit()

# Add columns for yfinance data and calculations
for row in trades:
    row['LTP']= None
    row['Calculation'] = None

# import data from yf

unique_symbols= []
start_date= '2024-02-01'
for symbol in unique_symbols:
    
    data = yf.download(symbol, start=start_date)
    data['Symbol'] = symbol
    historical_data = pd.concat([historical_data, data])
    historical_data.reset_index(inplace=True)

print(historical_data)

exit()


# # Step 4: Get yfinance data starting from 1st February
# symbols = trades['symbol'].unique()
# start_date = "2023-02-01"
# end_date = datetime.today().strftime('%Y-%m-%d')

# # Fetch LTP data for each symbol and store in the DataFrame
# for symbol in symbols:
#     data = yf.download(symbol + ".NS", start=start_date, end=end_date)
#     if not data.empty:
#         ltp = data['Close'][-1]  # Get the last closing price as LTP
#         trades.loc[trades['symbol'] == symbol, 'LTP'] = ltp

# # Step 5: Import other transaction data for calculations
# # Assuming columns for selling date, buying date, buying price, and quantity bought
# trades['buying_date'] = pd.to_datetime(trades['date'])  # Placeholder if missing data
# trades['selling_date'] = pd.to_datetime("2024-12-31")  # Placeholder if missing data
# trades['buying_price'] = trades['price']
# trades['quantity_bought'] = trades['qty']

# # Step 6: Calculate Profit/Loss based on the provided conditions
# def calculate_profit_loss(row):
#     current_date = pd.to_datetime(datetime.now().date())
#     if current_date < row['selling_date']:
#         if current_date >= row['buying_date']:
#             return (row['LTP'] - row['buying_price']) * row['quantity_bought']
#     return 0

# trades['Calculation'] = trades.apply(calculate_profit_loss, axis=1)

# # Step 7: Save to Excel and print the data
# trades.to_excel("updated_trades_with_LTP_and_PnL.xlsx", index=False)
# print("Data saved to 'updated_trades_with_LTP_and_PnL.xlsx'.")
