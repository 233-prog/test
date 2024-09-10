import json

# Sample JSON data
json_data = """
{
    "trades": [
        [
            {
                "dhanClientId": "1103599670",
                "orderId": "5124083056269",
                "exchangeOrderId": "1400000000497334",
                "exchangeTradeId": null,
                "transactionType": "BUY",
                "exchangeSegment": "NSE_EQ",
                "productType": "INTRADAY",
                "orderType": "MARKET",
                "tradingSymbol": null,
                "customSymbol": "Vodafone Idea",
                "securityId": "14366",
                "tradedQuantity": 620,
                "tradedPrice": 16.16,
                "isin": "INE669E01016",
                "instrument": "EQUITY",
                "sebiTax": 0.015,
                "stt": 8.0,
                "brokerageCharges": 1.49,
                "serviceTax": 0.3323,
                "exchangeTransactionCharges": 0.3264,
                "stampDuty": 1.0,
                "createTime": "NA",
                "updateTime": "NA",
                "exchangeTime": "2024-08-30 14:30:58",
                "drvExpiryDate": "NA",
                "drvOptionType": "NA",
                "drvStrikePrice": 0.0
            },
            {
                "dhanClientId": "1103599670",
                "orderId": "5124083056229",
                "exchangeOrderId": "1400000000497244",
                "exchangeTradeId": null,
                "transactionType": "SELL",
                "exchangeSegment": "NSE_EQ",
                "productType": "INTRADAY",
                "orderType": "MARKET",
                "tradingSymbol": null,
                "customSymbol": "Vodafone Idea",
                "securityId": "14366",
                "tradedQuantity": 620,
                "tradedPrice": 16.15,
                "isin": "INE669E01016",
                "instrument": "EQUITY",
                "sebiTax": 0.01,
                "stt": 0.0,
                "brokerageCharges": 2.98,
                "serviceTax": 0.5981,
                "exchangeTransactionCharges": 0.3224,
                "stampDuty": 0.0,
                "createTime": "NA",
                "updateTime": "NA",
                "exchangeTime": "2024-08-30 14:30:50",
                "drvExpiryDate": "NA",
                "drvOptionType": "NA",
                "drvStrikePrice": 0.0
            }
        ]
    ]
}
"""

# Convert JSON string to a Python dictionary
data = json.loads(json_data)

# Extract specific information
for trade_group in data['trades']:
    for trade in trade_group:
        # Filter only "BUY" transactions
        if trade['transactionType'] == "BUY":
            stock_name = trade['customSymbol']
            buying_price = trade['tradedPrice']
            quantity = trade['tradedQuantity']
            date_bought = trade['exchangeTime']

            print(f"Stock Name: {stock_name}, Buying Price: {buying_price}, Quantity: {quantity}, Date Bought: {date_bought}")

