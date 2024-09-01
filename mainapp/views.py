from django.shortcuts import render
from . import models


def index(request):
    testimonial = models.Testimonial.objects.all()
    return render(request, "mainapp/index.html", {'testimonial': testimonial})


def resume(request):
    return render(request, "mainapp/resume.html")


def portfolio(request):
    portfolioInfo = models.Portfolio.objects.all()
    return render(request, "mainapp/portfolio.html", {'portfolio': portfolioInfo})


def contact(request):
    return render(request, "mainapp/contact.html")
