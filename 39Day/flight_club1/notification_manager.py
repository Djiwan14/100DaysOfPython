from twilio.rest import Client

TWILIO_SID = 'ACd39011685649919678ce31cc5b7a391f'
TWILIO_AUTH_TOKEN = '019788ed5c05f0dcdd8bee558c3b49ad'
TWILIO_VIRTUAL_NUMBER = '+12057973283'
TWILIO_VERIFIED_NUMBER = '+36204190237'


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
