from django.db import models
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)  # Store latitude
    longitude = models.FloatField(null=True, blank=True)  # Store longitude

    def __str__(self):
        return self.name

