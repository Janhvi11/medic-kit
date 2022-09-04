from time import timezone
from django.db import models
from register.models import user
from django.utils import timezone
# Create your models here.

class timeline(models.Model):
    userId = models.ForeignKey(user, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now(), null=True)
    update = models.TextField(max_length=500)