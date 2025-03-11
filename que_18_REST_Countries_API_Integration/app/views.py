import requests
from django.shortcuts import render

def get_country_info(request):
    country_data = None
    error_message = None

    if request.method == 'POST':
        country_name = request.POST.get('country_name')

        if country_name:
            url = f"https://restcountries.com/v3.1/name/{country_name}"
            try:
                response = requests.get(url)
                country_data = response.json()[0]  

                population = country_data.get('population', 'N/A')
                languages = ', '.join(country_data.get('languages', {}).values())
                currency = ', '.join(country_data.get('currencies', {}).keys()) 

                country_info = {
                    'name': country_data.get('name', {}).get('common', 'N/A'),
                    'population': population,
                    'languages': languages,
                    'currency': currency
                }

            except requests.exceptions.RequestException as e:
                error_message = "An error occurred while fetching the country data."

    return render(request, 'demo.html', {
        'country_info': country_info if country_data else None,
        'error_message': error_message
    })
