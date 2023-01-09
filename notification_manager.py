from twilio.rest import Client

TWILIO_SID = "your sid here"
TWILIO_AUTH_TOKEN = "auth token here"
TWILIO_VIRTUAL_NUMBER = "Your virtual number here"
TWILIO_VERIFIED_NUMBER = "Your Number here"


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
