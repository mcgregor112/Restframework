from django.urls import path
from app.views import *

urlpatterns = [
    path('', get_coordinates, name='get_coordinates'),
]
