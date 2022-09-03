from django.urls import path
from ..views import *

to_do_url = [
    # path('home/', todo_home, name='users-home'),
    path('viewToDoList/', viewToDoList, name='todolist-view'),
    path('addToDoList/', addToDoList, name='todolist-add'),
    path('deleteToDoList/<id>', deleteToDoList, name='todolist-delete'),
    path('editToDoList/<id>', editToDoList, name='todolist-edit'),

]