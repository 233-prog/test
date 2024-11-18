import pandas as pd
from datetime import datetime, timedelta

# Define start date (1st February) and number of days (assuming for a month or user-specified)
start_date = datetime(2024, 2, 1)
num_days = 30  # Change as needed

# Create a DataFrame with a date column starting from 1st February
dates = [start_date + timedelta(days=i) for i in range(num_days)]
df = pd.DataFrame(dates, columns=['Date'])

# Create columns for Funds, Funds Balance, Realized P&L, Realized P&L Balance, and Net Profit
df['Funds'] = 0  # Initialize to 0; user can update these with actual data
df['Funds Balance'] = df['Funds'].cumsum()  # Cumulative sum of Funds
df['Realized P&L'] = 0  # Initialize to 0; user can update these with actual data
df['Realized P&L Balance'] = df['Realized P&L'].cumsum()  # Cumulative sum of Realized P&L
df['Net Profit'] = df['Funds Balance'] + df['Realized P&L Balance']  # Net profit calculation

# Example of how funds and realized P&L can be updated (user-specified data)
df.loc[0, 'Funds'] = 1000  # For example, $1000 added on 1st Feb
df.loc[5, 'Funds'] = 2000  # Another $2000 added on 6th Feb
df.loc[10, 'Realized P&L'] = 500  # $500 profit on 11th Feb

# Update calculated columns
df['Funds Balance'] = df['Funds'].cumsum()
df['Realized P&L Balance'] = df['Realized P&L'].cumsum()
df['Net Profit'] = df['Funds Balance'] + df['Realized P&L Balance']


output_file = 'financial_summary.xlsx'
df.to_excel(output_file, index=False)
print(f"Data exported to {output_file}")
