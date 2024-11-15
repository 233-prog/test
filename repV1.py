import yfinance as yf

# Define the stock ticker for TBZ (Tribhovandas Bhimji Zaveri Ltd)
ticker_symbol = "TBZ.NS"
stock = yf.Ticker(ticker_symbol)

# Fetch the most recent stock data and general info
data = stock.history(period="1y")
info = stock.info

# Fetch the stock data
stock = yf.Ticker(ticker_symbol)

# Get the exchange, sector, and last trading date
exchange = stock.info.get('exchange', 'N/A')
sector = stock.info.get('sector', 'N/A')

# Fetch the historical data and get the last trading date
hist = stock.history(period='1d', interval='1d')  # Get the most recent day
last_trading_day = hist.index[-1].date() if not hist.empty else 'No trading data'

# Get stock details
current_price = data['Close'][-1]
market_cap = info.get("marketCap")
year_high = data['High'].max()
year_low = data['Low'].min()
fifty_day_ma = data['Close'].rolling(window=50).mean().iloc[-1]
two_hundred_day_ma = data['Close'].rolling(window=200).mean().iloc[-1]
one_year_change = (current_price - data['Close'][0]) / data['Close'][0] * 100

# Calculate RSI
delta = data['Close'].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=14).mean().iloc[-1]
avg_loss = loss.rolling(window=14).mean().iloc[-1]
rs = avg_gain / avg_loss
rsi = 100 - (100 / (1 + rs))

# Get general financial info
info = stock.info

# Financial Statement Analysis
revenue = info.get("totalRevenue", "Data not available")
net_profit = info.get("netIncomeToCommon", "Data not available")
eps = info.get("trailingEps", "Data not available")

# Financial Ratios
pe_ratio = info.get("trailingPE", "Data not available")
pb_ratio = info.get("priceToBook", "Data not available")
de_ratio = info.get("debtToEquity", "Data not available")

# Get 1-year high, 1-year low, and 52-week change
one_year_high = stock.info.get('fiftyTwoWeekHigh', 'N/A')
one_year_low = stock.info.get('fiftyTwoWeekLow', 'N/A')
fifty_two_week_change = stock.info.get('52WeekChange', 'N/A')
current_price = stock.info.get('currentPrice', 'N/A')

# Determine trend based on the current price position and 52-week change
trend_comment = ""

if current_price != 'N/A' and one_year_high != 'N/A' and one_year_low != 'N/A':
    if current_price > one_year_high * 0.9:
        trend_comment = "The stock is close to its 1-year high, indicating a strong upward trend."
    elif current_price < one_year_low * 1.1:
        trend_comment = "The stock is near its 1-year low, indicating it may be on a downtrend."
    else:
        trend_comment = "The stock is trading in the middle of its 1-year range, suggesting stability or consolidation."

    # Further comments based on 52-week change
    if fifty_two_week_change != 'N/A':
        if fifty_two_week_change > 0:
            trend_comment += f" Over the past year, the stock has shown positive growth of {fifty_two_week_change * 100:.2f}%."
        else:
            trend_comment += f" Over the past year, the stock has declined by {abs(fifty_two_week_change) * 100:.2f}%."

else:
    trend_comment = "Insufficient data to determine the trend."
    
# Print report
print(f"Tribhovandas Bhimji Zaveri Ltd. (TBZ)")
print(f"Last Trading Day: {last_trading_day}")
print(f"Ticker: {ticker_symbol}")
print(f"Sector: {sector}")
print(f"Exchange: {exchange}")
print(f"Market Capitalization: ₹{market_cap / 1e7:.2f} crore (approx.)")
print(f"Current Stock Price: ₹{current_price:.2f} (as of recent closing)")

print("\nPrice History and Performance")
print(f"1-Year High: ₹{year_high:.2f}")
print(f"1-Year Low: ₹{year_low:.2f}")
print(f"52-Week Change: {one_year_change:.2f}%")

print("\nTechnical Indicators")
print(f"Relative Strength Index (RSI): {rsi:.2f}")
print(f"50-Day Moving Average: ₹{fifty_day_ma:.2f}")
print(f"200-Day Moving Average: ₹{two_hundred_day_ma:.2f}")
print(f"Trend Analysis: {trend_comment}")

# Print Financial Statement Analysis
print("Financial Statements Analysis")
print(f"Revenue: ₹{revenue / 1e7:.2f} crore (FY 2023)" if revenue != "Data not available" else "Revenue data not available")
print(f"Net Profit: ₹{net_profit / 1e7:.2f} crore" if net_profit != "Data not available" else "Net Profit data not available")
print(f"Earnings Per Share (EPS): ₹{eps:.2f}" if eps != "Data not available" else "EPS data not available")

# Print Financial Ratios
print("\nFinancial Ratios")
print(f"P/E Ratio: {pe_ratio}" if pe_ratio != "Data not available" else "P/E Ratio data not available")
print(f"P/B Ratio: {pb_ratio}" if pb_ratio != "Data not available" else "P/B Ratio data not available")
print(f"Debt-to-Equity Ratio: {de_ratio}" if de_ratio != "Data not available" else "Debt-to-Equity Ratio data not available")

