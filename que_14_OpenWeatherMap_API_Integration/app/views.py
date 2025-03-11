from django.shortcuts import render
import requests

def get_weather(request):
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.POST.get('city')
        if city:
            api_key = '39098d6124755c7a34f337690ccd6d50'  # Your OpenWeatherMap API key
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response = requests.get(url)

            if response.status_code == 200:
                weather_data = response.json()
            else:
                error_message = 'City not found or API error.'

    return render(request, 'weather/weather.html', {'weather_data': weather_data, 'error_message': error_message})
