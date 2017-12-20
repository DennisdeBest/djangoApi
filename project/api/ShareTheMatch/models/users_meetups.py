from django.db import models
from django.contrib.auth.models import User
from ..models import Meetup

class UsersMeetups(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    meetup = models.ForeignKey(Meetup, related_name='meetup', on_delete=models.CASCADE)
