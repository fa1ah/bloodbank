from django.db import models

# Create your models here.


class Bloody(models.Model):
    username = models.CharField(max_length=200)
    contact = models.IntegerField(default=0)
    blood = models.CharField(max_length=10, default='')
    email = models.EmailField(default='')
    # password = models.CharField(max_length=100, default='')
    firstname = models.CharField(max_length=100, default='')
    lastname = models.CharField(max_length=100, default='')
