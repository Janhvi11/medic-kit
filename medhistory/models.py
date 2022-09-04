from django.db import models

# Create your models here.
class medhistory(models.Model):
    #patient_id,patient_name(user)
    date = models.CharField(max_length=100)
    problems = models.CharField(max_length=50)
    prescription = models.CharField(max_length=50)
    