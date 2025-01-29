import yfinance as yf
import pandas as pd

# Define the stock ticker for TBZ (Tribhovandas Bhimji Zaveri Ltd)
ticker_symbol = "TBZ.NS"
stock = yf.Ticker(ticker_symbol)

# Fetch the most recent stock data and general info
data = stock.history(start='2024-10-29', end='2024-11-19', interval='1d')
info = stock.info


delta = data['Close'].diff()

gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=14).mean().iloc[-1]
avg_loss = loss.rolling(window=14).mean().iloc[-1]
rs = avg_gain / avg_loss
rsi = 100 - (100 / (1 + rs))

print(avg_gain)
print(avg_loss)

