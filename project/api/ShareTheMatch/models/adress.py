from django.db import models
from django.contrib.auth.models import User

class Adress(models.Model):
    user = models.ForeignKey(User, related_name='adresses', on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    post_code = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    place_id = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)