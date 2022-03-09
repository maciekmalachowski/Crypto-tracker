# Crypto tracker
----------------
This **Tracker** gets data from ``binance api`` using **requests** library, and then loads current and yesterday price of the given cryptocurrency.

After that it **sends an email** with an appropriate message, if the price is higher or lower than yesterday.

In order to send the email the program has to log in. In the ``.env`` file add:
```
email_adress = 'your_mail@gmail.com'
email_password = 'your_password'
```
In the meantime the name of cryptocurrency, price and time program writes to the file ``coin_price.txt``.
