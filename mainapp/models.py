from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    login = models.CharField(max_length=100)
    pasword=models.CharField(max_length=100)


    def __str__(self):
        return self.name