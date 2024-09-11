import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

# Define the ticker symbol for TBZ Jewellers
ticker_symbol = "TBZ.NS"  # Replace with the correct ticker symbol if needed

# Fetch OHLC data using yfinance
def fetch_ohlc_data(ticker_symbol, period="1mo", interval="1d"):
    data = yf.download(ticker_symbol, period=period, interval=interval)
    return data

# Plot candlestick chart
def plot_candlestick(data):
    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='Candlestick'
    )])

    fig.update_layout(
        title=f'Candlestick Chart for {ticker_symbol}',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis_rangeslider_visible=False
    )

    fig.show()

def main():
    # Fetch OHLC data
    data = fetch_ohlc_data(ticker_symbol)

    # Plot candlestick chart
    plot_candlestick(data)

if __name__ == "__main__":
    main()
