import os
from dotenv import load_dotenv
from twilio.rest import Client
from smtplib import SMTP

# load_dotenv(r"G:\My Drive\Programming\Python\EnvironmentVariables\.env.txt")
load_dotenv(r"C:\Users\watsorob\Google Drive\Programming\Python\EnvironmentVariables\.env.txt")

TWILIO_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
TWILIO_VERIFIED_NUMBER = os.getenv('MY_PHONE_NUMBER')
MAILTRAP_UN = os.getenv('MAILTRAP_UN')
MAILTRAP_PW = os.getenv('MAILTRAP_PW')

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_email(self, message, sender, receiver):
        message = message

        with SMTP("smtp.mailtrap.io", 587) as server:
            server.starttls()
            server.login("MAILTRAP_PW", "MAILTRAP_UN")
            server.sendmail(sender, receiver, message)
            print(server.ex)
