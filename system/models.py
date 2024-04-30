from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class register(models.Model):
    name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Email= models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    conformpassword=models.CharField(max_length=100)
class Deposit(models.Model):
    userid = models.IntegerField()
    rupee = models.IntegerField(default=100)
    date = models.DateField()
    time = models.TimeField()  
class Draw(models.Model):
    userid = models.IntegerField()
    rupee = models.IntegerField(default=100)
    date = models.DateField()
    time = models.TimeField()
class Win(models.Model):
    total=models.CharField(max_length=100)
    userid = models.IntegerField()
    eight = models.CharField(max_length=100)
    five = models.CharField(max_length=100)
    fifty = models.CharField(max_length=100)