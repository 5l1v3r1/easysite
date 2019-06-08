from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Buy(models.Model):
    food = models.CharField(max_length=100)
    email = models.EmailField()
   # portion = models.IntegerField()
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    fathername = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)

    def __str__(self):
       return self.adress