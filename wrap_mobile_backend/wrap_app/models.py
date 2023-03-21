from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    occupation = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    def __str__(self):
        return self.name


