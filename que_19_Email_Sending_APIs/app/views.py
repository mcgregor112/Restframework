from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm
from .utils import send_otp
from .models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            otp = send_otp(user.mobile)
            if otp is None:  # OTP sending failed
                messages.error(request, "Invalid phone number. Please enter a valid number with country code (e.g., +91878077XXXX).")
                return redirect('register')

            user.otp = otp
            user.is_verified = False
            user.save()
            messages.success(request, "OTP sent successfully. Please verify your account.")
            return redirect('verify_otp', user_id=user.id)
    
    else:
        form = UserRegistrationForm()

    return render(request, 'otp_app/register.html', {'form': form})

def verify_otp(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        entered_otp = request.POST.get('otp')

        if user.otp and user.otp == entered_otp:
            user.is_verified = True
            user.otp = None  
            user.save()

            messages.success(request, "Verification successful! Welcome.")
            return redirect('success') 

        messages.error(request, "Invalid OTP. Please try again.")

    return render(request, 'otp_app/verify_otp.html', {'user': user})
