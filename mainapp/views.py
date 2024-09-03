from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect

from . import models


@login_required
def index(request):
    testimonial = models.Testimonial.objects.all()
    return render(request, "mainapp/index.html", {'testimonial': testimonial})


@login_required
def resume(request):
    return render(request, "mainapp/resume.html")


@login_required
def portfolio(request):
    portfolioInfo = models.Portfolio.objects.all()
    return render(request, "mainapp/portfolio.html", {'portfolio': portfolioInfo})


@login_required
def contact(request):
    return render(request, "mainapp/contact.html")


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    error = ""
    username = ""
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if not username:
            error = "Введите username"
        elif not password:
            error = "Введите password"
        elif user is not None:
            login(request, user)
            return redirect('/')
        else:
            error = "Неправильный username или password"

    return render(request, "mainapp/login.html", {'error': error, "username": username})


def registration_view(request):
    error = ""
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if User.objects.filter(username=username).exists():
            error = "Пользователь с таким именем уже существует"
        elif not username:
            error = "Введите username"
        elif not password:
            error = "Введите password"
        elif password != password2:
            error = "Пароли должны быть похожи"
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('/')

    return render(request, "mainapp/register.html", {'error': error})
