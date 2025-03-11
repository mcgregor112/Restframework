import requests
from django.shortcuts import render
from django.conf import settings

def get_coordinates(request):
    coordinates = None
    error_message = None

    if request.method == "POST":
        address = request.POST.get('address')
        if address:
            api_key = settings.GOOGLE_MAPS_API_KEY
            url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200 and data['status'] == 'OK':
                coordinates = data['results'][0]['geometry']['location']
            else:
                error_message = 'Could not find coordinates for the given address.'

    return render(request, 'demo.html', {'coordinates': coordinates, 'error_message': error_message})

