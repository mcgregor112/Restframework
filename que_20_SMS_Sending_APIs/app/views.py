from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .utils import send_otp
from .models import User

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            otp = send_otp(user.mobile)
            user.otp = otp
            user.save()
            return redirect('verify_otp', user_id=user.id)
    else:
        form = UserRegistrationForm()
    return render(request, 'otp_app/register.html', {'form': form})

def verify_otp(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        if user.otp == entered_otp:
            user.is_verified = True
            user.save()
            return render(request, 'otp_app/success.html', {'user': user})
    return render(request, 'otp_app/verify_otp.html', {'user': user})



