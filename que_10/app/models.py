from django.db import models
import random

class sendotp(models.Model): 
    phone_number = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6)
    time = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def generate_otp():
        return str(random.randint(100000, 999999)) 
