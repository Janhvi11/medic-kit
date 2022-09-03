from django.urls import path
from ..views import *

disease_url = [
    path('diseaseView/', viewDisease, name="disease-view")
]