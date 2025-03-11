from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_appointment, name='book_appointment'),
    path('confirm_payment/', views.confirm_payment, name='confirm_payment'),
]