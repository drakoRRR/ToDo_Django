import requests
from django.shortcuts import render

# Create your views here.
def get_weather(city):
    appid = 'ff0053e1d0cf151dec66196a010149f1'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
    }

    return city_info


def get_client_city(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    response = requests.get(f'https://ipinfo.io/{ip}/json')
    data = response.json()

    if 'city' in data:
        return data['city']
    else:
        return 'London'


def main_page(request):
    '''Main page with the tasks'''

    city_info = get_weather(get_client_city(request))

    context = {
        'weather': city_info
    }

    get_client_city(request)

    return render(request, 'todo/mainpage.html', context)


def create_task(request):
    '''Page of creating tasks'''

    city_info = get_weather('London')

    context = {
        'weather': city_info
    }

    return render(request, 'todo/addtask.html', context)


