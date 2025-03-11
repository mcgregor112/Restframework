from twilio.rest import Client
import random
import re

def format_phone_number(mobile):
    """Ensure phone number is in E.164 format."""
    mobile = mobile.strip()
    if not re.match(r"^\+\d{10,15}$", mobile):
        return None
    return mobile

def send_otp(mobile):
    account_sid = 'AC48a8ad589c71f10b6b28726fd67d6dfd'
    auth_token = '12db800d53af87f246a7a7401af995af'
    twilio_phone = '+18562765875' 
    mobile = format_phone_number(mobile)
    if not mobile:
        return None 
    otp = str(random.randint(100000, 999999))

    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f'Your OTP is {otp}',
            from_=twilio_phone,
            to=mobile
        )
        return otp
    except Exception as e:
        print(f"Twilio Error: {e}")
        return None 
