from django.urls import path
from ..views import *

hosurl = [
    path('viewHos/', viewhos, name="view-hos"),
    path('addHos/', addhos, name="add-hos"),
    path('deleteHos/', viewhos, name="delete-hos"),
    path('editHos/', viewhos, name="edit-hos"),
]