from django.urls import path
from joke.views import *

urlpatterns = [
    path('',joke ,name='joke'),
    
]