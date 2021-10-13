from django.db import models

# Create your models here.

class Friend(models.Model):
    irum = models.CharField(max_length=10)  # CharField, TextField, DateTimeField, IntegerField, ...
    juso = models.CharField(max_length=20)
    nai = models.IntegerField()
    
