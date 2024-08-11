from django.shortcuts import render
from Users.forms import RegisterForm, LoginForm, RegisterLibrian


def register(request):
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def register_librian(request):
    form = RegisterLibrian()
    return render(request, 'register_librian.html', {'form': form})


def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})
