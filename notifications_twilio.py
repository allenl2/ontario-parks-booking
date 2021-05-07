from twilio.rest import Client
from notifications import getMessage
from dotenv import load_dotenv
import os

load_dotenv('.env')

account = 'AC2a1aed5804fe019e2d241a2765617ab3'
authToken = os.getenv('TWILIO_TOKEN')
client = Client(account, authToken)


def sendMessage():
    message = client.messages.create(
        messaging_service_sid='MG2b828d55f3f140c0fe57d6ecb3f96d42',
        body=getMessage(),
        to='+16479861235'
    )

    print(message.sid)
