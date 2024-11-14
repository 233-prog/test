import yfinance as yf

# Define the stock ticker for TBZ (Tribhovandas Bhimji Zaveri Ltd)
ticker_symbol = "TBZ.NS"
stock = yf.Ticker(ticker_symbol)

# Get general financial info
info = stock.info

# Financial Statement Analysis
revenue = info.get("totalRevenue", "Data not available")
net_profit = info.get("netIncomeToCommon", "Data not available")
eps = info.get("trailingEps", "Data not available")

# Financial Ratios
pe_ratio = info.get("trailingPE", "Data not available")
pb_ratio = info.get("priceToBook", "Data not available")
de_ratio = info.get("debtToEquity", "Data not available")

# Print Financial Statement Analysis
print("Financial Statements Analysis")
print(f"Revenue: ₹{revenue / 1e7:.2f} crore (FY 2023)" if revenue != "Data not available" else "Revenue data not available")
print(f"Net Profit: ₹{net_profit / 1e7:.2f} crore" if net_profit != "Data not available" else "Net Profit data not available")
print(f"Earnings Per Share (EPS): ₹{eps:.2f}" if eps != "Data not available" else "EPS data not available")

# Print Financial Ratios
print("\nFinancial Ratios")
print(f"P/E Ratio: {pe_ratio}" if pe_ratio != "Data not available" else "P/E Ratio data not available")
print(f"P/B Ratio: {pb_ratio}" if pb_ratio != "Data not available" else "P/B Ratio data not available")
print(f"Debt-to-Equity Ratio: {de_ratio}" if de_ratio != "Data not available" else "Debt-to-Equity Ratio data not available")
