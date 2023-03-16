from django.db import models
from django.contrib.auth.models import AbstractUser

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    occupation = models.CharField(max_length=100)