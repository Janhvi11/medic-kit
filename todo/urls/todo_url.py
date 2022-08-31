from django.urls import path
from ..views import *

to_do_url = [
    path('home/', todo_home, name='users-home'),
]