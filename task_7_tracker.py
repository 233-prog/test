import yfinance as yf
import numpy as np
import mplfinance as mpf
import matplotlib.pyplot as plt

# Fetch historical data for SHAKTIPUMP.NS
symbol = 'SHAKTIPUMP.NS'
data = yf.download(symbol, start='2023-01-01', end='2024-01-01', interval='1d')

# Display the fetched data
print(data.head())

# Plot candlestick chart
mpf.plot(data, type='candle', volume=True, title='SHAKTIPUMP.NS Candlestick Chart', style='yahoo')

def detect_ascending_staircase(data):
    closes = data['Close'].values
    return np.all(np.diff(closes) > 0)

def detect_descending_staircase(data):
    closes = data['Close'].values
    return np.all(np.diff(closes) < 0)

def detect_ascending_triangle(data):
    highs = data['High'].values
    lows = data['Low'].values
    upper_trendline = np.all(highs == highs.max())  # Flat upper trendline
    ascending_lower_trendline = np.all(np.diff(lows) > 0)  # Ascending lower trendline
    return upper_trendline and ascending_lower_trendline

def detect_descending_triangle(data):
    highs = data['High'].values
    lows = data['Low'].values
    lower_trendline = np.all(lows == lows.min())  # Flat lower trendline
    descending_upper_trendline = np.all(np.diff(highs) < 0)  # Descending upper trendline
    return lower_trendline and descending_upper_trendline

def detect_double_top(data):
    highs = data['High'].values
    peaks = (highs == highs.max()).sum()
    return peaks >= 2

# Determine the window of data to analyze (e.g., last 50 days)
window = data.tail(50)

patterns_detected = {
    'Ascending Staircase': detect_ascending_staircase(window),
    'Descending Staircase': detect_descending_staircase(window),
    'Ascending Triangle': detect_ascending_triangle(window),
    'Descending Triangle': detect_descending_triangle(window),
    'Double Top': detect_double_top(window)
}

# Print out which patterns were detected
for pattern, detected in patterns_detected.items():
    if detected:
        print(f"{pattern} pattern detected.")
    else:
        print(f"{pattern} pattern not detected.")

# Plot the candlestick chart with annotations
fig, ax = plt.subplots()
mpf.plot(data, type='candle', ax=ax, volume=True, style='yahoo', title='SHAKTIPUMP.NS Pattern Analysis')

# Annotate detected patterns
for pattern, detected in patterns_detected.items():
    if detected:
        # Find index for annotation
        if pattern == 'Double Top':
            # Annotate the highest peak (for simplicity)
            peak_index = np.argmax(data['High'].values)
            ax.annotate(f'{pattern} Detected', xy=(data.index[peak_index], data['High'][peak_index]),
                        xytext=(data.index[peak_index], data['High'][peak_index] + 10),
                        arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=10)
        else:
            # For other patterns, use a static index for demonstration
            ax.annotate(f'{pattern} Detected', xy=(data.index[-25], data['High'].max()),
                        xytext=(data.index[-50], data['High'].max() + 10),
                        arrowprops=dict(facecolor='green' if 'Ascending' in pattern else 'red', shrink=0.05),
                        fontsize=10)

plt.show()
