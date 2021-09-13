from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import authenticate, \
    login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.forms import UserCreationForm
from webpages.forms import CreateUserForm, LoginForm

from booking.models import Movie

def home(request):
    context = {
        'movies': Movie.objects.all()
    }
    return render(request, 'webpages/home.html', context)

def logout(request):
    auth_logout(request)
    return redirect('login')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = LoginForm()
    context = {'form': form}
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            username = User.objects.get(email=email).username

            # print(username, email, password)
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                raise Exception('Error occured while fetching details')
    except:
        context['error'] = 'Incorrect Credentials!'

    return render(request, 'webpages/login.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    # form = UserCreationForm()
    form = CreateUserForm()

    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered Successfully. Please Login !')
            return redirect('login')

    context = {'form': form}
    return render(request, 'webpages/register.html', context)


def movie(request, movie_id):
    context = {
        'movie': Movie.objects.get(id=movie_id),
        # 'is_authenticated': request.user.is_authenticated,
    }
    return render(request, 'webpages/movie.html', context)



