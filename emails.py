import smtplib
import imghdr
from email.message import EmailMessage
import os
from os.path import join, dirname
from dotenv import load_dotenv
from data_analysis import checkingData

class SendingEmail:
    def __init__(self):
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        self.adress = os.environ.get("email_adress")
        self.password = os.environ.get("email_password")
        
    def sendEmail(self, symbol, email_message):
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