from django.conf import settings
from django.db import models
from datetime import datetime,date
from django.contrib.auth.models import User


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,unique=True)
    email = models.EmailField(unique=True)
    # photo = models.ImageField(upload_to='profile_photos/',default='profile_photos/profile_user.png')
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=50,default='null')
    coins = models.IntegerField(default=0)
    occupation = models.CharField(max_length=20)

    def __str__(self):
        return self.email

class Booking(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE,default=0)
    book_id=  models.AutoField(primary_key=True)
    email = models.EmailField()
    uid = models.IntegerField()
    name = models.CharField(max_length=20,default='null')
    wastetype = models.CharField(max_length=20)
    date = models.DateField(settings.DATE_FORMAT)
    typeaddress = models.CharField(max_length=100)
    booking_address = models.CharField(max_length=100,default='null')
    booking_status = models.CharField(max_length=20)

    def __str__(self):
        return self.email

class WrapUser(models.Model) :
    wrapid=models.AutoField(primary_key=True)
    coins = models.IntegerField(default=0)

class PurchaseBin(models.Model) :
    pid = models.AutoField(primary_key=True)
    email = models.EmailField()
    uid = models.IntegerField()
    name = models.CharField(max_length=20,default='null')
    amount = models.IntegerField()
    address = models.CharField(max_length=50,default='null')
    returnsbin =  models.CharField(max_length=50,default='null')

class Redeem(models.Model) :
    rid = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='redeem_photos/')
    description = models.CharField(max_length=100)
    CHOICE_ONE = 'trending'
    CHOICE_TWO = 'ongoing'
    MY_CHOICES = [
        (CHOICE_ONE, 'trending'),
        (CHOICE_TWO, 'ongoing'),
    ]
    order_type = models.CharField(max_length=10, choices=MY_CHOICES)
    amount = models.IntegerField()


class Admin(models.Model):
    aid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)