from django import forms
from .models import *
 
class timelineForm(forms.ModelForm):
    class Meta:
        model = timeline
        fields=['userId','update']