from django.shortcuts import render
from .models import Testimonial


def index(request):
    testimonial = Testimonial.objects.all()
    return render(request, "mainapp/index.html", {'testimonial': testimonial})

def resume(request):
    return render(request, "mainapp/resume.html")

def portfolio(request):
    return render(request, "mainapp/portfolio.html")

def contact(request):
    return render(request, "mainapp/contact.html")

