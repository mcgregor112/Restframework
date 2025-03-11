from django.urls import path
from app.views import *

urlpatterns = [
    path('', send_sms, name='send_sms'),
]