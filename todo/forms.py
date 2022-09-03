from django import forms
from .models import *
 
class TodoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields="__all__"