from email import message
import smtplib
import imghdr
from email.message import EmailMessage
import os
from os.path import join, dirname
from dotenv import load_dotenv
from data import get_data


class SendingEmail:
    def __init__(self):
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        self.adress = os.environ.get("email_adress")
        self.password = os.environ.get("email_password")

    def checkingData(self):
        symbol, actual_price, price_at_10 = get_data()
        if float(actual_price) > (price_at_10):
            email_message = f"{symbol} cost more than at 10am by {round(actual_price-price_at_10, 3)}$"
        if float(actual_price) < (price_at_10):
            email_message = f"{symbol} cost less than at 10am by {round(price_at_10-actual_price, 3)}$"
        return symbol, email_message
        
    def sendEmail(self):
        symbol, email_message = self.checkingData()
        msg = EmailMessage()
        msg['Subject'] = f"{symbol} Notification"
        msg['From'] = self.adress
        msg['To'] = self.adress
        msg.set_content(f"{email_message}")

        with open('btc.png', 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.adress, self.password)
            smtp.send_message(msg)


x = SendingEmail()
x.sendEmail()