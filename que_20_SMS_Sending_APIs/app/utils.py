from twilio.rest import Client
import random

def send_otp(mobile):
    account_sid  = 'AC47e973ba9460fcf93c324289e1e5aabe'
    auth_token   = '72bc3f4cd2a275370175e07b9b735007'
    twilio_phone  = '+14173863192'

    otp = str(random.randint(100000, 999999))
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f'Your OTP is {otp}',
        from_=twilio_phone,
        to=mobile
    )
    return otp