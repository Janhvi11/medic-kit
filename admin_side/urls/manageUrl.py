from django.urls import path
from ..views import *

m_url = [
    path('viewDoc/', viewDoc, name="view-doc"),
    path('editDoc/<username>', editDoc, name="edit-doc"),
    path('deleteDoc/<username>', deleteDoc, name="delete-doc"),
    path('addDoc/', addDoc, name="add-doc"),
]