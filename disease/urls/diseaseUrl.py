from django.urls import path
from ..views import *

disease_url = [
    path('diseaseView/', viewDisease, name="disease-view"),
    path('diseaseEdit/<id>', editDisease, name="disease-edit"),#id
    path('diseaseDelete/<id>', deleteDisease, name="disease-delete"),#
    path('diseaseAdd/', addDisease, name="disease-add"),
]