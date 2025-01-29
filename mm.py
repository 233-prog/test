def calculate_trend(current_price, one_year_high, one_year_low):
    if one_year_high == 'N/A' or one_year_low == 'N/A' or current_price == 'N/A':
        return "Insufficient data to determine the trend."

    
    position = (current_price - year_low) / (year_high - year_low) * 100

    
    if position >= 80:
        return "The stock is in a strong uptrend, near its 1-year high."
    elif 60 <= position < 80:
        return "The stock shows a moderate uptrend, trending upward but not at its peak."
    elif 40 <= position < 60:
        return "The stock price is stable, trading around the middle of its 1-year range."
    elif 20 <= position < 40:
        return "The stock shows a moderate downtrend, below the midpoint of its 1-year range."
    else position < 20
        return "The stock is in a strong downtrend, near its 1-year low."
    
    print(position)