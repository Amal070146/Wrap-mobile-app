from django.conf import settings
from django.db import models
from datetime import datetime,date
from django.contrib.auth.models import User


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='profile_photos/',default='profile_photos/profile_user.png')
    password = models.CharField(max_length=20)


class Admin(models.Model):
    aid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)