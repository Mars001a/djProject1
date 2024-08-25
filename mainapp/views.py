from django.shortcuts import render
from .models import User


def index(request):
    data = User.objects.all()
    return render(request, "mainapp/index.html", {'data': data})

