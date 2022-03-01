import requests
import json
import datetime

def get_data(symbol):
    try:
        r = requests.get(f"https://www.binance.com/api/v3/ticker/price?symbol={symbol}")
        candle = requests.get(f"https://www.binance.com/api/v1/klines?symbol={symbol}&interval=1d")

        values = r.json()
        print(values['symbol'], values['price'])
        symbol = values['symbol']
        price = float(values['price'])

        candle_values = candle.json()
        price_yesterday = float(candle_values[-2][4])#closing

        now = datetime.datetime.now()
        now = now.strftime("%H:%M:%S")
        with open('coin_price.txt', 'a') as f:
            f.write(f"{symbol},{price},{now}\n")
        return symbol, price, price_yesterday

    except Exception as e:
        print(f"{str(e)} is wrong.")
        return None, None, None
    

