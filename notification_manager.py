from twilio.rest import Client
import os

TWILIO_ACCOUNT= os.environ.get('TWILIO_ACCOUNT')
TWILIO_TOKEN= os.environ.get('TWILIO_TOKEN')
TWILIO_NUMBER= os.environ.get('TWILIO_NUMBER')
MY_NUMBER= os.environ.get('MY_NUMBER')

account_sid = TWILIO_ACCOUNT
auth_token = TWILIO_TOKEN

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    def send_notification(self):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Deal alert from {self.origin_city}, {self.origin_airport} to {self.destination_city}, {self.destination_airport} for {self.price} from the {self.out_date} to {self.return_date} ",
            from_= TWILIO_NUMBER,
            to= MY_NUMBER
        )
        print(message.sid)










