from django.urls import path
from ..views import *

bmi_url_def = [
    path('viewbmi/', viewbmi, name="bmi-view"),
    path('addbmi/', addbmi, name="bmi-add"),
    path('editbmi<id>/', editbmi, name="bmi-edit"),
    path('deletebmi<id>/', deletebmi, name="bmi-delete"),
    
    path('viewidealbmi/', viewidealbmi, name="ideal-bmi-view"),
    path('addidealbmi/', addidealbmi, name="ideal-bmi-add"),
    path('editidealbmi<id>/', editidealbmi, name="ideal-bmi-edit"),
    path('deleteidealbmi<id>/', deleteidealbmi, name="ideal-bmi-delete"),
]