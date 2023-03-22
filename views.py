from django.http import JsonResponse
import requests

def get_weather(request):
    city = request.GET.get('city')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY'
    response = requests.get(url)
    data = response.json()
    weather_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    }
    return JsonResponse(weather_data)
