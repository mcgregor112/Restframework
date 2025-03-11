from django.urls import path
from app.views import *

urlpatterns = [
    path('', latest_tweets, name='latest_tweets'),
]
