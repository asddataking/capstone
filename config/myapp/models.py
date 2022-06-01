from django.db import models
from django.contrib.auth.models import AbstractUser

class MyModel(models.Model):
    myfield = models.CharField(max_length=200)
    
    
class User(AbstractUser):
    pass


class Pet (models.Model):
    
    pet_types = (
    ('dog','DOG'),
    ('cat', 'CAT'),
)
    
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=6, choices=pet_types,  default='dog')

    
