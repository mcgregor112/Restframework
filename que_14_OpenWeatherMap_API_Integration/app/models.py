from django.db import models

# Create your models here.
class WeatherQuery(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    humidity = models.IntegerField(null=True, blank=True)  # New field
    created_at = models.DateTimeField(auto_now_add=True)
