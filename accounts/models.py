from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    buyer = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pet = models.ManyToManyField('pets.Pet')
    def __str__(self):
        return str(self.buyer)
