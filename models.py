from django.db import models

# # Create your models here.
class post(models.Model):
    Email = models.CharField(max_length=250)
    Password = models.CharField(max_length=250)
    Server  = models.CharField(max_length=250)
    Port = models.CharField(max_length=250)
