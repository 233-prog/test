from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf

# Sample trades dictionary
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



# Step 2: Read Sheet3 data for additional symbols if required (assuming it's part of the same workbook)
# If already in trades list, you might skip this step if not needed.
# sheet3_data = pd.read_excel("your_file.xlsx", sheet_name="Sheet3")
# trades = pd.concat([trades, sheet3_data], ignore_index=True)

# Step 3: Add columns for yfinance data, dates, and calculations
trades['LTP'] = None
trades['date'] = pd.to_datetime(trades['date'])
trades['Calculation'] = None

# Step 4: Get yfinance data starting from 1st February
symbols = trades['symbol'].unique()
start_date = "2023-02-01"
end_date = datetime.today().strftime('%Y-%m-%d')

# Fetch LTP data for each symbol and store in the DataFrame
for symbol in symbols:
    data = yf.download(symbol + ".NS", start=start_date, end=end_date)
    if not data.empty:
        ltp = data['Close'][-1]  # Get the last closing price as LTP
        trades.loc[trades['symbol'] == symbol, 'LTP'] = ltp

# Step 5: Import other transaction data for calculations
# Assuming columns for selling date, buying date, buying price, and quantity bought
trades['buying_date'] = pd.to_datetime(trades['date'])  # Placeholder if missing data
trades['selling_date'] = pd.to_datetime("2024-12-31")  # Placeholder if missing data
trades['buying_price'] = trades['price']
trades['quantity_bought'] = trades['qty']

# Step 6: Calculate Profit/Loss based on the provided conditions
def calculate_profit_loss(row):
    current_date = pd.to_datetime(datetime.now().date())
    if current_date < row['selling_date']:
        if current_date >= row['buying_date']:
            return (row['LTP'] - row['buying_price']) * row['quantity_bought']
    return 0

trades['Calculation'] = trades.apply(calculate_profit_loss, axis=1)

# Step 7: Save to Excel and print the data
trades.to_excel("updated_trades_with_LTP_and_PnL.xlsx", index=False)
print("Data saved to 'updated_trades_with_LTP_and_PnL.xlsx'.")
