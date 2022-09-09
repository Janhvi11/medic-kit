from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #
from .models import *

class AppointmentForm(forms.ModelForm):
# not null field define karna
    class Meta:
        model = appointment
        fields = '__all__'