from django.urls import path
from ..views import *

feed_url = [
    path('viewFeedback/',viewFeedback,name="view-feedback"),
    path('deleteFeedback<id>/',deleteFeedback,name="delete-feedback"),
    path('addFeedback/',addFeedback,name="add-feedback"),
    path('download',download_csv,name='download'),

]