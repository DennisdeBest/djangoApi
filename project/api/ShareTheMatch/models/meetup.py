from django.db import models
from django.contrib.auth.models import User
from ..models import Adress

class Meetup(models.Model):
    user = models.ForeignKey(User, related_name='meetups', on_delete=models.CASCADE)
    adress = models.ForeignKey(Adress, related_name='meetups', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateField()
    places_available = models.IntegerField()