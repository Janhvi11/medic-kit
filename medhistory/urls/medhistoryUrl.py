from django.urls import path
from ..views import *

medhistory_url = [
    path('medhistoryView/', viewMedhistory, name="medhistory-view"),
    path('medhistoryEdit/<id>', editMedhistory, name="medhistory-edit"),#id
    path('medhistoryDelete/<id>', deleteMedhistory, name="medhistory-delete"),#
    path('medhistoryAdd/', addMedhistory, name="medhistory-add"),
    path('download',download_csv,name='download'),

]