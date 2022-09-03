from django import forms
from .models import *

class TodoListForm(forms.ModelForm):
    class Meta:
        model = disease
        fields="__all__"