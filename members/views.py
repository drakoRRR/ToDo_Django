from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_page(request):
    '''Sign up page'''

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('main')
        else:
            messages.success(request, 'There was an error logging in, Try again...')
            return redirect('login')
    else:
        return render(request, 'members/login.html')


def logout_page(request):
    ''''''
    logout(request)
    messages.success(request, 'You Were Logged out!')
    return redirect('main')


def register_page(request):
    '''Sign in page'''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration Successful!')
            return redirect('main')
    else:
        form = UserCreationForm()

    return render(request, 'members/register.html', {'form': form})