import yfinance as yf

# Define the ticker symbol for TBZ Jewellers
ticker_symbol = "TBZ.NS"  # Replace with the correct ticker symbol for your exchange if different

# Download OHLC data using yfinance
# You can adjust the period (e.g., "1mo", "1y") and interval (e.g., "1d", "1wk") as needed
data = yf.download(ticker_symbol, period="1mo", interval="1d")

# Display the OHLC data
print("OHLC Data for TBZ Jewellers:")
print(data)
