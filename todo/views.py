import requests
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

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

    tasks = Task.objects.all()
    city_info = get_weather(get_client_city(request))

    context = {
        'weather': city_info,
        'tasks': tasks,
    }

    get_client_city(request)

    return render(request, 'todo/mainpage.html', context)


def create_task(request):
    '''Page of creating tasks'''

    error = ''

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Wrong form'

    city_info = get_weather('London')
    form = TaskForm()

    context = {
        'weather': city_info,
        'form': form,
        'error': error,
    }

    return render(request, 'todo/addtask.html', context)


def login_page(request):
    '''Sign up page'''
    return render(request, 'todo/login_reg_pages/login.html')


def register_page(request):
    return render(request, 'todo/login_reg_pages/register.html')


def delete_task(request, task_id):
    task_to_delete = Task.objects.get(id=task_id)
    task_to_delete.delete()
    return redirect('main')