
from twilio.rest import Client
import os

# this class is responsible for sending SMS notifications with the deal flight details.
    # def check_if_Google_sheet_is_lowest_price(self):

# retrieve Twilio credentials and phone numbers from environment variables:
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
from_your_virtual_twilio_phone_number = os.environ.get("FROM_YOUR_VIRTUAL_TWILIO_PHONE_NUMBER")
to_recipient_phone_number = os.environ.get("TO_RECIPIENT_PHONE_NUMBER")

class NotificationManager:
    pass