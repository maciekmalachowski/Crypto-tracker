from data import get_data
from emails import SendingEmail
from data_analysis import checkingData
import sys
import time

start_time = time.time()
run_time = 30
# symbol, price, price_yesterday = get_data(sys.argv[1])

print(f"Program will run for {run_time} seconds.")

if len(sys.argv) == 1:
    sys.argv.append("BTCUSDT")
symbol, price, price_yesterday = get_data(sys.argv[1])

while True:
    if (time.time() - start_time) > run_time:
        break
    if symbol is None:
        print("Try again. If this persists, contact the developer. Program is ending.")
        sys.exit(1)

    email_message = checkingData(symbol, price, price_yesterday)
    time.sleep(10)

x = SendingEmail()
x.sendEmail(symbol, email_message)