from django.urls import path
from ..views import *

m_url = [
    path('viewDoc/', viewDoc, name="view-doc"),
    path('editDoc/<username>', editDoc, name="edit-doc"),
    path('deleteDoc/<username>', deleteDoc, name="delete-doc"),
    path('addDoc/', addDoc, name="add-doc"),

    path('viewPharma/', viewPharma, name="view-pharma"),
    path('editPharma/<username>', editPharma, name="edit-pharma"),
    path('deletePharma/<username>', deletePharma, name="delete-pharma"),
    path('addPharma/', addPharma, name="add-pharma"),
]