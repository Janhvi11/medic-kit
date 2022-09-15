from django.db import models
from django.utils import timezone

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=50, default="admin")
    type = models.IntegerField()
    
class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now(),blank=True,null=True)
    due_date = models.DateTimeField(default=one_week_hence, blank=True, null=True)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)