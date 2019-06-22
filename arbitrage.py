import ccxt 

exchange_list = {"coincheck" : {
                    "apiKey":"",
                    "serect":""
                 },
                 "bitflyer" : {
                     "apiKey":"",
                     "serect":""
                 },
                 "zaif" : {
                     "apiKey":"",
                     "serect":""
                 }
}

amount = 0.001
ask_exchange = ''
ask_price = 1000000000
bid_exchange = ''
bid_price = 0

for exchange_id in exchange_list:
    exchange = eval('ccxt.' + exchange_id + '()')

    orderbook = exchange.fetch_order_book('BTC/JPY')
    ask = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None
    bid = orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None

    if ask < ask_price:
        ask_exchange = exchange_id
        ask_price = ask
    if bid > bid_price:
        bid_exchange = exchange_id
        bid_price = bid

ask_price = int(ask_price/5)*5
exchange = eval('ccxt.' + ask_exchange + '()') 
exchange.apiKey = exchange_list[ask_exchange]["apiKey"]
exchange.serect = exchange_list[ask_exchange]["serect"]
exchange.create_limit_buy_order('BTC/JPY', amount, ask_price)

bid_price = int(bid_price/5)*5
exchange = eval('ccxt.' + bid_exchange + '()')
exchange.apiKey = exchange_list[bid_exchange]["apiKey"]
exchange,serect = exchange_list[bid_exchange]["serect"]
exchange.create_limit_sell_order('BTC/JPY', amount, bid_price)

print( ask_exchange + 'で' + ask_price + '円を' + amount + 'だけ買って')
print( bid_exchange + 'で' + bid_price + '円を' + amount + 'だけ売ると')
print((ask_price - bid_price)*amount + " 円の利益")