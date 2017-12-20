from django.db import models
from ..models import Meetup

class Sport(models.Model):
    meetup = models.ForeignKey(Meetup, related_name='Sports', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    supported_team = models.CharField(max_length=100)