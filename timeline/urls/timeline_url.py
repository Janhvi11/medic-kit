from django.urls import path
from ..views import *

time_url = [
    path('viewTimeline/', viewTime, name="view-time"),
    path('editTimeline<id>/', editTime, name="edit-time"),
    path('addTimeline/', addTime, name="add-time"),
    path('deleteTimeline<id>/', deleteTime, name="delete-time"),
]