from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #
#from .models import *
from appointment.models import *


class AppointmentForm(forms.ModelForm):
# not null field define karna
    class Meta:
        model = Appointment
        fields = ['fname','lname','email','address','time','day','request','status']

# 'fname','lname','email','address','time','day','request','status'


#class AcceptAppointmentForm(forms.ModelForm):
## not null field define karna
#    class Meta:
#        model = acceptappointment
#        fields = '__all__'