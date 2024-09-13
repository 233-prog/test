import yfinance as yf

# Fetch historical data for TBZ.NS
symbol = 'SHAKTIPUMP.NS'
data = yf.download(symbol, start='2023-01-01', end='2024-01-01', interval='1d')

# Display the fetched data
print(data.head())
import talib
import numpy as np

# Extract OHLC data from the fetched data
open_prices = data['Open'].values
high_prices = data['High'].values
low_prices = data['Low'].values
close_prices = data['Close'].values

# Detect patterns using TA-Lib functions
ascending_triangle = talib.CDLASCENDINGTRIANGLE(open_prices, high_prices, low_prices, close_prices)
descending_triangle = talib.CDLDESCENDINGTRIANGLE(open_prices, high_prices, low_prices, close_prices)
double_top = talib.CDLDOUBLETOP(open_prices, high_prices, low_prices, close_prices)
ascending_staircase = talib.CDLUPSIDEGAP2CROWS(open_prices, high_prices, low_prices, close_prices)
descending_staircase = talib.CDLDOWNSIDEGAP2CROWS(open_prices, high_prices, low_prices, close_prices)

# Store detected patterns
patterns = {
    'Ascending Triangle': ascending_triangle,
    'Descending Triangle': descending_triangle,
    'Double Top': double_top,
    'Ascending Staircase': ascending_staircase,
    'Descending Staircase': descending_staircase
}

# Find the indices where patterns are detected (TA-Lib returns 100 or -100 for pattern matches)
detected_patterns = {pattern: np.where(value != 0)[0] for pattern, value in patterns.items()}

# Print out the detected patterns
for pattern, indices in detected_patterns.items():
    if len(indices) > 0:
        print(f"{pattern} detected at index positions: {indices}")
    else:
        print(f"{pattern} not detected.")
import mplfinance as mpf
import matplotlib.pyplot as plt

# Plot candlestick chart
fig, ax = plt.subplots()
mpf.plot(data, type='candle', ax=ax, volume=True, style='yahoo', title='TBZ.NS Pattern Analysis')

# Annotate the detected patterns
for pattern, indices in detected_patterns.items():
    for index in indices:
        ax.annotate(pattern, xy=(data.index[index], data['High'][index]),
                    xytext=(data.index[index], data['High'][index] + 10),
                    arrowprops=dict(facecolor='green' if 'Ascending' in pattern else 'red', shrink=0.05),
                    fontsize=8)

plt.show()
