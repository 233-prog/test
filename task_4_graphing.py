import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

# Define the ticker symbol for TBZ Jewellers
ticker_symbol = "TBZ.NS"  # Replace with the correct ticker symbol if needed

# Fetch OHLC data using yfinance
def fetch_ohlc_data(ticker_symbol, start_date, end_date, interval="1h"):
    data = yf.download(ticker_symbol, start=start_date, end=end_date, interval=interval)
    return data

# Plot candlestick chart
def plot_candlestick(data, ticker_symbol):
    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='Candlestick',
        increasing_line_color='green',   # Set color for increasing candles
        decreasing_line_color='red',     # Set color for decreasing candles
        increasing_fillcolor='lightgreen', # Fill color for increasing candles
        decreasing_fillcolor='lightcoral'  # Fill color for decreasing candles
    )])

    # Update layout for better visibility and continuous pattern
    fig.update_layout(
        title=f'Candlestick Chart for {ticker_symbol}',
        xaxis_title='Date and Time',
        yaxis_title='Price',
        xaxis_rangeslider_visible=False,
        xaxis_type='category',  # Set x-axis type to category for continuous plotting
        width=1000,  # Width of the figure
        height=600,  # Height of the figure
        plot_bgcolor='white',  # Background color
        yaxis=dict(
            gridcolor='lightgrey',  # Gridline color
            gridwidth=0.5           # Gridline width
        ),
        xaxis=dict(
            gridcolor='lightgrey',
            gridwidth=0.5
        ),
        margin=dict(l=50, r=50, t=50, b=50)  # Margins around the plot
    )

    fig.show()

def main():
    # Set the date range
    start_date = "2023-08-01"  # Set your start date
    end_date = "2023-08-31"    # Set your end date

    # Fetch OHLC data
    data = fetch_ohlc_data(ticker_symbol, start_date, end_date, interval="1h")

    # Plot candlestick chart
    plot_candlestick(data, ticker_symbol)

if __name__ == "__main__":
    main()
