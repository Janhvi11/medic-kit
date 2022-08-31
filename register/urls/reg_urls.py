from django.urls import path
from ..views import *

reg_url_list = [
    path('home/', reg_home, name='users-home'),
    path('main/', MainView.as_view(), name='main-view'), 
    path('register/', RegisterView.as_view(), name='users-register'), 
]