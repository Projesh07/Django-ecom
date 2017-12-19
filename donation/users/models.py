from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.TextField(blank=True)
    provider = models.CharField(max_length=100, blank=True)
    provider_id = models.CharField(max_length=255, blank=True)