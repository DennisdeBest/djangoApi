from django.db import models
from ..models import Adress

class Stuff(models.Model):
    adress = models.ForeignKey(Adress, related_name='stuffs', on_delete=models.CASCADE)
    tv = models.CharField(max_length=100)
    sits = models.CharField(max_length=500)