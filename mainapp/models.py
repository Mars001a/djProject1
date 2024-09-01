from django.db import models


class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    text = models.TextField()
    img = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=200, blank=True)
    href = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
