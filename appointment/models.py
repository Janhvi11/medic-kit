from django.db import models

# Create your models here.



time = (
    ('10:00-11:00','10:00-11:00'),
    ('11:00-12:00','11:00-12:00'),
    ('12:00-1:00','12:00-1:00'),
    ('1:00-2:00','1:00-2:00'),
    ('2:00-3:00','2:00-3:00'),
    ('3:00-4:00','3:00-4:00'),
    ('4:00-5:00','4:00-5:00'),
    ('5:00-6:00','5:00-6:00'),
)

day = (
    ('MONDAY','MONDAY'),
    ('TUESDAY', 'TUESDAY'),
    ('WEDNESDAY','WEDNESDAY'),
    ('THURSDAY','THURSDAY'),
    ('FRIDAY','FRIDAY'),
    ('SATURDAY','SATURDAY'),
    ('SUNDAY','SUNDAY'),
)


class appointment(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    time = models.CharField(max_length=500,choices=time)
    day = models.CharField(max_length=500,choices=day)
    request = models.TextField(max_length=500)