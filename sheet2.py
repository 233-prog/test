import yfinance as yf
import pandas as pd
from datetime import datetime

# Step 1: Define stock symbols and trades
stocks = ['VOLTAS.NS', 'INDIANHUME.NS', 'ASTRAMICRO.NS', 'GULPOLY.NS', 'SHAKTIPUMP.NS']
trades = [
    # Your list of trades goes here (as provided)
]

# Step 2: Function to fetch daily stock prices
def fetch_stock_prices(symbols):
    prices = {}
    for symbol in symbols:
        # Fetch the latest stock data
        stock_data = yf.download(symbol, period='1d')
        # Get the closing price for the day
        if not stock_data.empty:
            closing_price = stock_data['Close'].values[0]
            prices[symbol] = closing_price
        else:
            prices[symbol] = None
    return prices

# Step 3: Pairing logic from the provided code
def pair_trades(trades):
    pair_num = 1
    for trade in trades:
        trade['pair'] = ''
    
    for sell_trade in trades:
        if sell_trade['type'] == 'SELL':
            symbol = sell_trade['symbol']
            sell_qty = sell_trade['qty']
            pair_made = False

            # Loop through the buy trades
            for buy_trade in trades:
                if buy_trade['pair'] == '' and buy_trade['symbol'] == symbol and buy_trade['type'] == 'BUY':
                    buy_qty = buy_trade['qty']
                    if abs(buy_qty) <= abs(sell_qty):
                        sell_qty = sell_qty + buy_qty
                        buy_trade['pair'] = pair_num
                        sell_trade['pair'] = pair_num
                        pair_made = True
                    else:
                        if abs(sell_qty) > 0:
                            # Split the buy trade into two trades
                            new_buy_qty = buy_qty + sell_qty
                            new_buy_amt = new_buy_qty * buy_trade['price'] * -1
                            new_buy_trade = buy_trade.copy()
                            new_buy_trade['qty'] = new_buy_qty
                            new_buy_trade['amt'] = new_buy_amt

                            # Update the original buy trade
                            buy_trade['qty'] = abs(sell_qty)
                            buy_trade['amt'] = abs(sell_qty) * buy_trade['price'] * -1

                            # Add the new buy trade to the trades list
                            trades.append(new_buy_trade)
                            trades = sorted(trades, key=lambda x: x['date'])

                            sell_qty = 0
                            buy_trade['pair'] = pair_num
                            sell_trade['pair'] = pair_num
                            pair_made = True

            if pair_made:
                pair_num += 1

    return trades

# Step 4: Main logic
if __name__ == "__main__":
    # Fetch the latest stock prices
    stock_prices = fetch_stock_prices(stocks)
    
    # Pair the trades
    paired_trades = pair_trades(trades)
    
    # Create a DataFrame for the trades
    df = pd.DataFrame(paired_trades)
    
    # Add a column for the latest stock price
    df['latest_price'] = df['symbol'].apply(lambda symbol: stock_prices.get(symbol + '.NS', 'N/A'))
    
    # Save to Excel
    file_name = f'stock_pairs_{datetime.now().strftime("%Y-%m-%d")}.xlsx'
    df.to_excel(file_name, index=False)
    print(f"Data saved to {file_name}")
