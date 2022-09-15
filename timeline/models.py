from time import timezone
from django.db import models
from register.models import user,doc,pharma
from django.utils import timezone
# Create your models here.

class timeline(models.Model):
    userId = models.ForeignKey(user, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now(), null=True)
    update = models.TextField(max_length=500)
    type=models.CharField(max_length=20, default="user", null=True, blank=True)
    
class timeline_doc(models.Model):
    docId = models.ForeignKey(doc, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now(), null=True)
    update = models.TextField(max_length=500)
    type=models.CharField(max_length=20, default="doc", null=True, blank=True)
    
class timeline_pharma(models.Model):
    pharmaId = models.ForeignKey(pharma, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now(), null=True)
    update = models.TextField(max_length=500)
    type=models.CharField(max_length=20, default="pharma", null=True, blank=True)