import pandas as pd
from datetime import datetime

# Define the data (you can replace with your actual data)
data = {
    "Date": [datetime(2024, 10, 2), datetime(2024, 10, 3)],
    "Funds": [10000, 12000],
    "Funds Balance": [15000, 18000],
    "Realized P&L": [2000, 2500],
    "Realized P&L Balance": [22000, 24000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate Net Profit (Funds Balance + Realized P&L)
df["Net Profit"] = df["Funds Balance"] + df["Realized P&L"]

# Export the DataFrame to Excel
file_name = 'financial_data.xlsx'
df.to_excel(file_name, index=False)

print(f"Data exported successfully to {file_name}")
