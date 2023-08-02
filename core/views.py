import requests
import pip._vendor.requests 
import os
from dotenv import load_dotenv
from django.shortcuts import render
load_dotenv()

API_KEY = os.environ.get('API_KEY')
print(API_KEY)
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def home(request):
    if 'location' in request.GET:
        location = request.GET['location'] 
        # print (location)
        weather_data = get_weather_data(location)
        context = {'weather_data': weather_data, 'location': location}
        return render(request, 'core/index.html', context)
    else:
        default_location = "Nepal"
        weather_data = get_weather_data(default_location)
        context = {'weather_data': weather_data, 'location': default_location}
        # print(context)
        return render(request, 'core/index.html', context)