from django.db import models
from ..custom_permissions import IsOwnerOrAdmin

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('created')