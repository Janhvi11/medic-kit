from django.db import models
from register.models import *
from django.utils import timezone

# Create your models here.

class chat(models.Model):
    senderId = models.CharField(max_length=256)
    receiverId = models.CharField(max_length=256)
    message = models.CharField(max_length=256)
    date = models.DateField(default=timezone.now(), null=True)