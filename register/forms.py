from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #
from .models import *

class RegisterForm(forms.ModelForm):
# not null field define karna
    class Meta:
        model = user
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'address']

class RegisterDocForm(forms.ModelForm):
# not null field define karna
    class Meta:
        model = doc
        fields = ['name', 'age', 'experience', 'hosName', 'hosLocation', 'email', 'degree', 'phone', 'username','password']

class RegisterPharmaForm(forms.ModelForm):
# not null field define karna
    class Meta:
        model = pharma
        fields = ['name', 'shopName', 'shopAddr', 'licenseNumber', 'city', 'nationwideDel', 'username', 'password', 'email']


###
class LoginUserForm(forms.Form):    
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50)
    # remember_me = forms.BooleanField(required=False)

    class Meta:
        model = user
        fields = ['username', 'password']