from django.shortcuts import render
from django.http.response import JsonResponse
import requests

# Create your views here.


def joke(request):

    external_api = "https://official-joke-api.appspot.com/jokes/random"

    response = requests.get(external_api)
    response.raise_for_status()

    joke_data = response.json()

    return render(request, 'joke.html' , {"joke" : joke_data})
