import requests
import json
from urllib import request
import datetime

def get_data():
    try:
        r = requests.get("https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT")

        values = r.json()
        print(values['symbol'], values['price'])
        symbol = values['symbol']
        price = float(values['price'])

        price_at_10 = 38382.72000000
        now = datetime.datetime.now()
        now = now.strftime("%H:%M:%S")
        f = open('coin_price.txt', 'a')
        f.write(f"{symbol}, {price}, time: {now}; \n")
        return symbol, price, price_at_10

    except:
        print("Somethink wrong :( Try later.")
