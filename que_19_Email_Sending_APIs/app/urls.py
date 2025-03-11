from django.urls import path  
from django.shortcuts import redirect 
from . import views  

urlpatterns = [
    path('', lambda request: redirect('register')),
    path('register/', views.register, name='register'),
    path('verify-otp/<int:user_id>/', views.verify_otp, name='verify_otp'),
]
