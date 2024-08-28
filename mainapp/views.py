from django.shortcuts import render
from .models import User


def index(request):
    data = User.objects.all()
    return render(request, "mainapp/index.html", {'data': data})

def resume(request):
    return render(request, "mainapp/resume.html")

def portfolio(request):
    return render(request, "mainapp/portfolio.html")

def contact(request):
    return render(request, "mainapp/contact.html")

