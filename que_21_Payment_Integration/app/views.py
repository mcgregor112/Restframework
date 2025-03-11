import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import AppointmentBookingForm

stripe.api_key = settings.STRIPE_SECRET_KEY

def book_appointment(request):
    if request.method == "POST":
        form = AppointmentBookingForm(request.POST)
        if form.is_valid():
            # Get form data
            doctor_name = form.cleaned_data['doctor_name']
            appointment_date = form.cleaned_data['appointment_date']
            amount = form.cleaned_data['amount'] * 100  # Stripe expects amount in cents

            # Create a Payment Intent
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
                metadata={'doctor_name': doctor_name, 'appointment_date': str(appointment_date)},
            )

            return render(request, 'payment.html', {
                'client_secret': intent.client_secret,
                'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY,
                'amount': amount / 100,
            })
    else:
        form = AppointmentBookingForm()

    return render(request, 'appointment_form.html', {'form': form})

def confirm_payment(request):
    if request.method == 'POST':
        payment_intent_id = request.POST['payment_intent_id']
        payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)

        if payment_intent['status'] == 'succeeded':
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'failed'})

    return JsonResponse({'status': 'invalid'})

