import yfinance as yf
import pandas as pd

input_json = [
    {"Symbol": "INDUSTOWER", "Min": 425, "Max": 450},
    {"Symbol": "IREDA", "Min": 200, "Max": 250},
    {"Symbol": "RVNL", "Min": 500, "Max": 575},
    {"Symbol": "SUZLON", "Min": 45, "Max": 60},
    {"Symbol": "COCHINSHIP", "Min": 1750, "Max": 2200}
]

for stock in  input_json:
    symbol= stock["Symbol"]+".NS"
    min= stock ["Min"]
    max= stock ["Max"]

data = yf.download(ticker_symbol, start=start_date, end=end_date, interval="1d")

