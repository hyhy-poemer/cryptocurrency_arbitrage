import ccxt

print(ccxt.exchanges)
# bitflyer = ccxt.bitflyer()
# orderbook = bitflyer.fetch_order_book('BTC/JPY')
# bid = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None
# ask = orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None
# spread = (ask - bid) if (bid and  ask) else None
# print (bitflyer.id, 'market price', {'bid' : bid, 'ask' : ask, 'spread' : spread})


# exchange_list = ['coincheck', 'bitflyer', 'zaif']

# for exchange_id in exchange_list:
#     exchange = eval('ccxt.' + exchange_id + '()')
#     orderbook = exchange.fetch_order_book('BTC/JPY')
#     bid = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None
#     ask = orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None
#     spread = (ask - bid) if (bid and  ask) else None
#     print (exchange_id, 'market price', {'bid' : bid, 'ask' : ask, 'spread' : spread})


