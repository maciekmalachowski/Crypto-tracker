# Crypto tracker
----------------
## How it works
This **Tracker** gets data from ``Binance api`` using **requests** library, and then loads current and yesterday price of the given cryptocurrency.

After that it **sends an email** with an appropriate message, if the price is higher or lower than yesterday.

In order to send the email the program has to log in. Create ``.env`` file and add there:
```
email_adress = 'your_mail@gmail.com'
email_password = 'your_password'
```
In the meantime the name of cryptocurrency, price and time program writes to the file ``coin_price.txt``.

## Setup 
To use it you have to go to the `Crypto-tracker\tracker` directory in the console:
```
C:\Users\user> cd Crypto-tracker\tracker
```
Then just start `tracker.py` in console.
```
C:\Users\user\Crypto-tracker\tracker> python tracker.py
```
## Error with sending emails
You may have an error related to your email. That's becaouse google blocks some activities on mail.

In this case you should `turn on` less secure apps option at this link https://myaccount.google.com/lesssecureapps.
