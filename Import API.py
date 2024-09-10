import http.client

conn = http.client.HTTPSConnection("api.dhan.co")

headers = {
    'access-token': "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzI4NDg1MTYzLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMzU5OTY3MCJ9.q7bbzSc5jMi16mQBdWSFmVHVXZlYoVTWDTedsvnnRsBkk7XgjLB7_vRIgmeSB5pI7QTZnNWps1lQ064GyzpX-w",
    'Accept': "application/json"
}

conn.request("GET", "/tradeHistory/2024-08-01/2024-08-31/0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
