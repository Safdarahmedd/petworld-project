from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    vacc = (('y','yes'),('n','no'))
    name = models.CharField(max_length=128)
    breed = models.CharField(max_length=64)
    vaccinated = models.CharField(max_length=1, choices = vacc)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

class Img(models.Model):
    info = models.ForeignKey(Pet, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
