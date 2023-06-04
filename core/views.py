import requests
import pip._vendor.requests 
from django.shortcuts import render

API_KEY = 'afcde0ca355ba4fe4fc0947b41892bf0'

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

def home(request):
    if 'location' in request.GET:
        location = request.GET['location'] 
        print (location)
        weather_data = get_weather_data(location)
        context = {'weather_data': weather_data, 'location': location}
        return render(request, 'core/index.html', context)
    else:
        # If no location is provided, show default location
        default_location = "Nepal"
        weather_data = get_weather_data(default_location)
        context = {'weather_data': weather_data, 'location': default_location}
        print(context)
        return render(request, 'core/index.html', context)