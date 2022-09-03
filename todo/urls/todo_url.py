from django.urls import path
from ..views import *

to_do_url = [
    # path('home/', todo_home, name='users-home'),
    path('viewToDoList/', viewToDoList, name='todolist-view'),
    path('addToDoList/', addToDoList, name='todolist-add'),
    path('deleteToDoList/<id>', deleteToDoList, name='todolist-delete'),
    path('editToDoList/<id>', editToDoList, name='todolist-edit'),

]

to_do_item_url = [
    # path('home/', todo_home, name='users-home'),
    path('viewToDoItem/<id> ', viewToDoItem, name='todoItem-view'),
    path('addToDoItem/', addToDoItem, name='todoItem-add'),
    path('deleteToDoItem/<id>', deleteToDoItem, name='todoItem-delete'),
    path('editToDoItem/<id>', editToDoItem, name='todoItem-edit'),

]