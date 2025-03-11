from django.shortcuts import render
from django.http import JsonResponse
from app.models import sendotp
from twilio.rest import Client
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import re 

@csrf_exempt
def send_sms(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        
        if not phone_number:
            return JsonResponse({'error': 'Phone number is required'}, status=400)
        phone_number = phone_number.strip()
        if not phone_number.startswith("+"):
            phone_number = "+91" + phone_number  
        if not re.match(r'^\+\d{10,15}$', phone_number):
            return JsonResponse({'error': 'Invalid phone number format'}, status=400)

        otp_obj, created = sendotp.objects.get_or_create(
            phone_number=phone_number,
            defaults={'otp': sendotp.generate_otp()}
        )

        if not created:
            otp_obj.otp = sendotp.generate_otp()
            otp_obj.save()

        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        try:
            client.messages.create(
                body=f'Your OTP is {otp_obj.otp}',
                from_=settings.TWILIO_MOBILE_NUMBER,
                to=phone_number 
            )
            return JsonResponse({'message': 'OTP sent successfully', 'otp': otp_obj.otp})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'demo.html')
