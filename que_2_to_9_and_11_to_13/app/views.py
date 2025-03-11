from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Doctor
from app.serializer import DoctorSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated


class DoctorPagination(PageNumberPagination):
    page_size = 2  
    page_size_query_param = 'page_size'
    max_page_size = 10


class DoctorAPIView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        doctors = Doctor.objects.all()
        paginator = DoctorPagination()
        result_page = paginator.paginate_queryset(doctors, request)
        serializer = DoctorSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CRUDAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def doctor_view(request):
    doctors = Doctor.objects.all()
    return render(request, 'profile.html', {'doctors': doctors})
