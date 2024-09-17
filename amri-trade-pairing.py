
trades = [
    {'date': '2023-04-18', 'symbol': 'VOLTAS', 'type': 'BUY', 'qty': 39, 'price': 1311.00, 'amt': -51129.00},
    {'date': '2023-05-17', 'symbol': 'INDIANHUME', 'type': 'BUY', 'qty': 800, 'price': 323.96, 'amt': -259170.00},
    {'date': '2023-05-24', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'BUY', 'qty': 1000, 'price': 799.98, 'amt': -799980.00},
    {'date': '2023-05-27', 'symbol': 'VOLTAS', 'type': 'BUY', 'qty': 211, 'price': 1424.88, 'amt': -300650.00},
    {'date': '2023-06-13', 'symbol': 'VOLTAS', 'type': 'SELL', 'qty': -39, 'price': 1480.55, 'amt': 57741.00},
    {'date': '2023-06-13', 'symbol': 'VOLTAS', 'type': 'SELL', 'qty': -211, 'price': 1480.55, 'amt': 312396.00},
    {'date': '2023-06-13', 'symbol': 'GULPOLY', 'type': 'BUY', 'qty': 1500, 'price': 214.20, 'amt': -321300.00},
    {'date': '2023-07-11', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'BUY', 'qty': 1000, 'price': 927.50, 'amt': -927500.00},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -201, 'price': 900.00, 'amt': 180900.00},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -5, 'price': 899.80, 'amt': 4499.00},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -92, 'price': 899.70, 'amt': 82772.40},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -4, 'price': 899.65, 'amt': 3598.60},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -351, 'price': 899.60, 'amt': 315759.60},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -4, 'price': 899.55, 'amt': 3598.20},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -11, 'price': 899.50, 'amt': 9894.50},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -8, 'price': 899.45, 'amt': 7195.60},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -69, 'price': 899.40, 'amt': 62058.60},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -30, 'price': 899.35, 'amt': 26980.50},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -55, 'price': 899.30, 'amt': 49461.50},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -8, 'price': 899.25, 'amt': 7194.00},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -16, 'price': 899.20, 'amt': 14387.20},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -18, 'price': 899.15, 'amt': 16184.70},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -12, 'price': 899.10, 'amt': 10789.20},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -116, 'price': 899.05, 'amt': 104289.80},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -38, 'price': 899.05, 'amt': 34163.90},
    {'date': '2023-07-19', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -149, 'price': 899.00, 'amt': 133951.00},
    {'date': '2023-07-22', 'symbol': 'ASTRA MICROWAVE LTD', 'type': 'SELL', 'qty': -813, 'price': 904.00, 'amt': 734952.00},
    {'date': '2023-08-06', 'symbol': 'SHAKTIPUMP', 'type': 'BUY', 'qty': 350, 'price': 4785.66, 'amt': -1674981.00}
]

for trade in trades:
    trade['pair'] = ''

pair_num = 1

for sell_trade in trades:
    if sell_trade['type'] == 'SELL':

        symbol = sell_trade['symbol']
        sell_qty = sell_trade['qty']

        pair_made = False

        # loop through the buy trades
        for buy_trade in trades:
            if buy_trade['pair'] == '' and buy_trade['symbol'] == symbol and buy_trade['type'] == 'BUY':
                buy_qty = buy_trade['qty']
                if abs(buy_qty) <= abs(sell_qty):
                    sell_qty = sell_qty + buy_qty
                    buy_trade['pair'] = pair_num
                    sell_trade['pair'] = pair_num
                    pair_made = True

                else:
                    if abs(sell_qty) > 0:

                        # split the buy trade into two trades
                        new_buy_qty = buy_qty + sell_qty
                        new_buy_amt = new_buy_qty * buy_trade['price'] * -1
                        new_buy_trade = buy_trade.copy()
                        new_buy_trade['qty'] = new_buy_qty
                        new_buy_trade['amt'] = new_buy_amt

                        # update the original buy trade
                        buy_trade['qty'] = abs(sell_qty)
                        buy_trade['amt'] = abs(sell_qty) * buy_trade['price'] * -1

                        # add the new buy trade to the trades list
                        trades.append(new_buy_trade)
                        trades = sorted(trades, key=lambda x: x['date'])

                        sell_qty = 0
                        buy_trade['pair'] = pair_num
                        sell_trade['pair'] = pair_num
                        pair_made = True

        if pair_made:
            pair_num += 1
        
# write the trades to a excel file using pd
import pandas as pd

df = pd.DataFrame(trades)
df.to_excel('trades.xlsx', index=False)