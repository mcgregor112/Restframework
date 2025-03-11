from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    speciality =models.CharField(max_length=255)
    contact = models.TextField()
