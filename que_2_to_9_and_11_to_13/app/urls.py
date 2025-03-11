from django.urls import path
from app.views import DoctorAPIView, CRUDAPIView, doctor_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('doctors/', DoctorAPIView.as_view(), name='doctor_api'),
    path('doctors/<int:pk>/', CRUDAPIView.as_view(), name='crud_api'),
    path('', doctor_view, name='doctor_view'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
