from django.urls import path
from app.views import *

urlpatterns = [
    path('', get_country_info, name='country_info'),
]


