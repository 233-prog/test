import pandas as pd
from datetime import datetime, timedelta
import yfinance as yf

# -------------------------------
# Step 1: Define and Process Trades
# -------------------------------

# Define the list of trades
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

# Convert 'date' from string to datetime objects
for trade in trades:
    trade['date'] = pd.to_datetime(trade['date'])

# Initialize 'pair' field
for trade in trades:
    trade['pair'] = ''

pair_num = 1

# Process trades to pair BUY and SELL
for sell_trade in trades:
    if sell_trade['type'] == 'SELL':
        symbol = sell_trade['symbol']
        sell_qty = abs(sell_trade['qty'])  # Absolute value for comparison

        pair_made = False

        # Loop through the buy trades to find a match
        for buy_trade in trades:
            if buy_trade['pair'] == '' and buy_trade['symbol'] == symbol and buy_trade['type'] == 'BUY':
                buy_qty = buy_trade['qty']

                if buy_qty <= sell_qty:
                    sell_qty -= buy_qty
                    buy_trade['pair'] = pair_num
                    sell_trade['pair'] = pair_num
                    pair_made = True
                else:
                    # Split the buy trade
                    new_buy_qty = buy_qty - sell_qty
                    new_buy_amt = new_buy_qty * buy_trade['price'] * -1
                    new_buy_trade = buy_trade.copy()
                    new_buy_trade['qty'] = new_buy_qty
                    new_buy_trade['amt'] = new_buy_amt
                    new_buy_trade['pair'] = ''

                    # Update the original buy trade
                    buy_trade['qty'] = sell_qty
                    buy_trade['amt'] = sell_qty * buy_trade['price'] * -1
                    buy_trade['pair'] = pair_num

                    # Append the new buy trade to the list
                    trades.append(new_buy_trade)
                    trades = sorted(trades, key=lambda x: x['date'])

                    # Assign pair to sell trade
                    sell_trade['pair'] = pair_num
                    pair_made = True
                    sell_qty = 0

                if sell_qty == 0:
                    break

        if pair_made:
            pair_num += 1

# -------------------------------
# Step 2: Create DataFrame for Paired Trades
# -------------------------------

# Convert trades list to DataFrame
df_trades = pd.DataFrame(trades)

# Filter out trades that are not part of any pair
df_pairs = df_trades[df_trades['pair'] != '']

# Organize paired trades
paired_trades = df_pairs.sort_values(by='pair')

# Select relevant columns
paired_trades = paired_trades[['pair', 'date', 'symbol', 'type', 'qty', 'price', 'amt']]

# Reset index
paired_trades.reset_index(drop=True, inplace=True)

# -------------------------------
# Step 3: Map Symbols to Exchanges and YFinance Tickers
# -------------------------------

# Define a mapping of symbols to their respective exchanges
# Update this dictionary based on actual exchange listings
symbol_exchange = {
    'VOLTAS': 'NSE',
    'INDIANHUME': 'NSE',
    'ASTRA MICROWAVE LTD': 'NSE',
    'GULPOLY': 'NSE',
    'SHAKTIPUMP': 'NSE'
    # Add more symbols and their exchanges as needed
}

# Define a separate mapping for symbols with non-standard YFinance tickers
symbol_yf_mapping = {
    'ASTRA MICROWAVE LTD': 'ASTRAMICRO.NS'
    # Add more exceptions as needed
}

# Function to get yfinance ticker with exchange suffix or special mapping
def get_yf_ticker(symbol):
    if symbol in symbol_yf_mapping:
        return symbol_yf_mapping[symbol]
    exchange = symbol_exchange.get(symbol, 'NSE')  # Default to NSE if not mapped
    if exchange == 'NSE':
        return f"{symbol}.NS"
    elif exchange == 'BSE':
        return f"{symbol}.BO"
    else:
        return symbol  # If exchange is unknown, return the symbol as is

# Get unique symbols from paired trades
unique_symbols = paired_trades['symbol'].unique()

# Create a dictionary to map symbols to yfinance tickers
symbol_to_yf = {symbol: get_yf_ticker(symbol) for symbol in unique_symbols}

# -------------------------------
# Step 4: Fetch Historical Data
# -------------------------------

# Define the date range for the past 3 months
end_date = datetime.today()
start_date = end_date - timedelta(days=90)  # Approximately 3 months

historical_data = {}

for symbol, yf_ticker in symbol_to_yf.items():
    try:
        # Fetch historical data
        ticker = yf.Ticker(yf_ticker)
        hist = ticker.history(start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))

        if hist.empty:
            print(f"No historical data found for {symbol}.")
            historical_data[symbol] = pd.DataFrame()  # Empty DataFrame
        else:
            hist.reset_index(inplace=True)
            # Remove timezone information if present
            if hist['Date'].dtype == 'datetime64[ns, UTC]':
                hist['Date'] = hist['Date'].dt.tz_localize(None)
            else:
                hist['Date'] = pd.to_datetime(hist['Date']).dt.tz_localize(None)
            hist['Symbol'] = symbol  # Add symbol column
            historical_data[symbol] = hist
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        historical_data[symbol] = pd.DataFrame()  # Empty DataFrame

# -------------------------------
# Step 5: Prepare Historical Data for Excel
# -------------------------------

# Initialize an empty list to collect DataFrames
historical_data_frames = []

for symbol, data in historical_data.items():
    if not data.empty:
        historical_data_frames.append(data)
    else:
        # Create a blank DataFrame with the necessary columns
        blank_df = pd.DataFrame({
            'Date': [pd.NaT],
            'Open': [pd.NA],
            'High': [pd.NA],
            'Low': [pd.NA],
            'Close': [pd.NA],
            'Volume': [pd.NA],
            'Dividends': [pd.NA],
            'Stock Splits': [pd.NA],
            'Symbol': [symbol]
        })
        historical_data_frames.append(blank_df)

# Concatenate all historical data into a single DataFrame
df_historical = pd.concat(historical_data_frames, ignore_index=True)

# Sort historical data by symbol and date
df_historical.sort_values(by=['Symbol', 'Date'], inplace=True)
df_historical.reset_index(drop=True, inplace=True)

# -------------------------------
# Step 6: Export to Excel
# -------------------------------

# Create a Pandas Excel writer using openpyxl as the engine
file_name = f"trade_and_historical_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
    # Export paired trades to "Pairs" sheet
    paired_trades.to_excel(writer, sheet_name='Pairs', index=False)
    
    # Export historical data to "Historical Data" sheet
    df_historical.to_excel(writer, sheet_name='Historical Data', index=False)

print(f"Data exported successfully to {file_name}")
