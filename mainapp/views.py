from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
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
        print(username)
        print(password)
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
