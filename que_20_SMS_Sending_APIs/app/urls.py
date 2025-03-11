from django.urls import path
from app.views import *

urlpatterns = [
    path('', register, name='register'),
    path('verify-otp/<int:user_id>/', verify_otp, name='verify_otp'),
]
