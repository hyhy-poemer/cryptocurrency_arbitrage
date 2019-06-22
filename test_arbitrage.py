import ccxt

exchange_list = ['bitflyer','coincheck', 'bitbank','zaif']
ask_exchange = ''
ask_price = 999999999
bid_exchange = ''
bid_price = 0

for exchange_id in exchange_list:
    exchange = eval('ccxt.' + exchange_id + '()')
    orderbook = exchange.fetch_order_book('BTC/JPY')
    bid = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None
    ask = orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None
    if ask < ask_price:
        ask_exchange = exchange_id
        ask_price = ask
    if bid > bid_price:
        bid_exchange = exchange_id
        bid_price = bid

print(ask_exchange, 'で', ask_price, ' 円で買って')
print(bid_exchange, 'で', bid_price, ' 円で売れば')
print(bid_price - ask_price, ' 円の利益')