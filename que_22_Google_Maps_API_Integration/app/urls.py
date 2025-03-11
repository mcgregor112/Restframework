from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_locations, name='doctor_locations'),
]
