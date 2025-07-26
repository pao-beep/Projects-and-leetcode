from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from datetime import datetime


# Create your views here.
#This file will contain all the application's logic e.g., capturing data from the form, sending a request to the API, etc. 
def index(request):
    #return HttpResponse('The Index View')

    #the render function is for rendering templates
    #return render(request,'weatherupdates/home.html')
    try:
        if request.method == 'POST':
            API_KEY = 'c47c5fb737bdb19b7acce7ac8b9ed2c1'
            # getting the city name from the form input
            city_name = request.POST.get('city')
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
            # converting the request response to json
            response = requests.get(url).json()
            #getting the current time
            current_time = datetime.now()
            # formatting the time using directives, it will take this format Day, Month Date Year, Current Time 
            formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
            
            city_weather_update = {
                'city' : city_name,
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'temperature': 'Temperature: ' + str(response['main']['temp']) + ' C',
                'country_code': response['sys']['country'],
                'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
                'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
                'time': formatted_time
            }
        else:
            city_weather_update = {}
        context = {'city_weather_update':city_weather_update}
        return render(request,'weatherupdates/home.html', context)
    
    except:
        return render(request,'weatherupdates/404/html')




