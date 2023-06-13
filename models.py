from django.db import models

# Create your models here.

class contact_up(models.Model):
  name = models.CharField(max_length=30)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=30)
  message = models.TextField(max_length=50)
  
class user(models.Model):
  email = models.CharField(max_length=30)
  password = models.CharField(max_length=20)
  username = models.CharField(max_length=30)
  otp = models.IntegerField(default=1234)