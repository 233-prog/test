import http.client

conn = http.client.HTTPSConnection("api.dhan.co")

headers = {
    'access-token': "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzI4NDg1MTYzLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMzU5OTY3MCJ9.q7bbzSc5jMi16mQBdWSFmVHVXZlYoVTWDTedsvnnRsBkk7XgjLB7_vRIgmeSB5pI7QTZnNWps1lQ064GyzpX-w",
    'Accept': "application/json"
}

conn.request("GET", "/tradeHistory/2024-08-01/2024-08-31/0", headers=headers)

res = conn.getresponse()
data = res.read()

# print(data.decode("utf-8"))

import json

json_data = str(data.decode("utf-8"))

print(json_data)

# # Sample JSON data
# json_data = """
# {
#     "trades": [
#         [
#             {
#                 "dhanClientId": "1103599670",
#                 "orderId": "5124083056269",
#                 "exchangeOrderId": "1400000000497334",
#                 "exchangeTradeId": null,
#                 "transactionType": "BUY",
#                 "exchangeSegment": "NSE_EQ",
#                 "productType": "INTRADAY",
#                 "orderType": "MARKET",
#                 "tradingSymbol": null,
#                 "customSymbol": "Vodafone Idea",
#                 "securityId": "14366",
#                 "tradedQuantity": 620,
#                 "tradedPrice": 16.16,
#                 "isin": "INE669E01016",
#                 "instrument": "EQUITY",
#                 "sebiTax": 0.015,
#                 "stt": 8.0,
#                 "brokerageCharges": 1.49,
#                 "serviceTax": 0.3323,
#                 "exchangeTransactionCharges": 0.3264,
#                 "stampDuty": 1.0,
#                 "createTime": "NA",
#                 "updateTime": "NA",
#                 "exchangeTime": "2024-08-30 14:30:58",
#                 "drvExpiryDate": "NA",
#                 "drvOptionType": "NA",
#                 "drvStrikePrice": 0.0
#             },
#             {
#                 "dhanClientId": "1103599670",
#                 "orderId": "5124083056229",
#                 "exchangeOrderId": "1400000000497244",
#                 "exchangeTradeId": null,
#                 "transactionType": "SELL",
#                 "exchangeSegment": "NSE_EQ",
#                 "productType": "INTRADAY",
#                 "orderType": "MARKET",
#                 "tradingSymbol": null,
#                 "customSymbol": "Vodafone Idea",
#                 "securityId": "14366",
#                 "tradedQuantity": 620,
#                 "tradedPrice": 16.15,
#                 "isin": "INE669E01016",
#                 "instrument": "EQUITY",
#                 "sebiTax": 0.01,
#                 "stt": 0.0,
#                 "brokerageCharges": 2.98,
#                 "serviceTax": 0.5981,
#                 "exchangeTransactionCharges": 0.3224,
#                 "stampDuty": 0.0,
#                 "createTime": "NA",
#                 "updateTime": "NA",
#                 "exchangeTime": "2024-08-30 14:30:50",
#                 "drvExpiryDate": "NA",
#                 "drvOptionType": "NA",
#                 "drvStrikePrice": 0.0
#             }
#         ]
#     ]
# }
# """

# Convert JSON string to a Python dictionary
data2 = json.loads(json_data)

# Extract specific information
for trade_group in data2['trades']:
    for trade in trade_group:
        # Filter only "BUY" transactions
        if trade['transactionType'] == "BUY":
            stock_name = trade['customSymbol']
            buying_price = trade['tradedPrice']
            quantity = trade['tradedQuantity']
            date_bought = trade['exchangeTime']

            print(f"Stock Name: {stock_name}, Buying Price: {buying_price}, Quantity: {quantity}, Date Bought: {date_bought}")
