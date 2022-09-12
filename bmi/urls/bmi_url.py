from django.urls import path
from ..views import *

bmi_url = [
    path('viewbmi/', viewbmi, name="bmi-view"),
    path('addbmi/', addbmi, name="bmi-add"),
    path('editbmi<id>/', deletebmi, name="bmi-edit"),
    path('deletebmi<id>/', editbmi, name="bmi-delete"),
]