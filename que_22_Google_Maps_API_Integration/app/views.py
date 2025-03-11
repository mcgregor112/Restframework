# views.py
from django.shortcuts import render
from .models import Doctor
import googlemaps
from django.conf import settings

def doctor_locations(request):
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

    doctors = Doctor.objects.all()

    # Update coordinates for doctors without latitude/longitude
    for doctor in doctors:
        if doctor.city and (doctor.latitude is None or doctor.longitude is None):
            try:
                geocode_result = gmaps.geocode(doctor.city)
                if geocode_result:
                    doctor.latitude = geocode_result[0]['geometry']['location']['lat']
                    doctor.longitude = geocode_result[0]['geometry']['location']['lng']
                    doctor.save()
            except Exception as e:
                print(f"Error fetching geolocation for {doctor.city}: {e}")

    context = {
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY,
        'doctors': doctors,
    }

    return render(request, 'doctor_map.html', context)


