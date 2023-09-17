import requests
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from django.contrib import messages

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

    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
    else:
        tasks = []

    city_info = get_weather(get_client_city(request))

    context = {
        'weather': city_info,
        'tasks': tasks,
    }

    return render(request, 'todo/mainpage.html', context)


def create_task(request):
    '''Page of creating tasks'''

    error = ''

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  # Создайте задачу, но не сохраняйте ее в базе данных пока
            task.user = request.user  # Свяжите задачу с текущим пользователем
            task.save()  # Теперь сохраните задачу в базе данных

            # Добавьте задачу в сессию пользователя
            if 'tasks' not in request.session:
                request.session['tasks'] = []

            request.session['tasks'].append(task.id)

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


def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        if task.user == request.user:
            task.delete()

            # Удалите задачу из сессии пользователя
            if 'tasks' in request.session and task_id in request.session['tasks']:
                request.session['tasks'].remove(task_id)

            messages.success(request, 'Task deleted successfully.')
        else:
            messages.error(request, 'You do not have permission to delete this task.')
    except Task.DoesNotExist:
        messages.error(request, 'Task does not exist.')

    return redirect('main')

