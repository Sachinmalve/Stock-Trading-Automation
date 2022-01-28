import logging
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

kite = KiteConnect(api_key="your_api_key")

data = kite.generate_session("request_token_here", secret="your_secret")
kite.set_access_token(data["access_token"])

kws = KiteTicker("your_api_key", "your_access_token")

def on_ticks(kws, ticks):

    logging.debug("Ticks: {}".format(ticks))

def on_connect(kws, response):

    kws.subscribe([738561, 5633])


    kws.set_mode(kws.MODE_FULL, [738561])

def on_close(ws, code, reason):

    kws.stop()

kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

kws.connect()

kws.subscribe(kws.get_insturment_by_symbol('NSE','Nifty Bank'  ), LiveFeedType.Maket_DATA  )

bn_call = kws.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2022, 2, 24), is_fut=False, strike=ATMStrike + 200, is_CE = True)
bn_put = kws.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2022, 2, 24), is_fut=False, strike=ATMStrike - 200, is_CE = False)
Search for symbols


#for placing order of strangle with 20% stoploss

def place_order(transaction_type,symbol) :
                      qty = int (symbol.lot_size)
                      res=kws.place_order(transaction_type=TransactionType.Sell,
                      instrument= symbol,
                      quantity=qty,
                      order_type=OrderType.Market,
                      product_type=ProductType.Delivery,
                      price=0.0,
                      trigger_price=None,
                      stop_loss= .20,
                      square_off=None,
                      trailing_sl=None,
                      is_amo=False)

print (res)
place_order(TransactionType.Sell,ce_strike)
