from django.urls import path
from ..views import *

login_url = [
    path('login/', login_home, name='login-home'),
    path('loginuser/', login_request, name='user-login'),
    path('logindoctor/', login_home, name='doc-login'),
    path('loginpharma/', login_home, name='pharma-login'),
]

# redirect_authenticated_user=True, 