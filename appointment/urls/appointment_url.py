from django.urls import path
from ..views import *

appointmenturl = [
    path('viewappointment/', viewAppointment, name="appointment-view"),
    path('deleteappointment<id>/', deleteAppointment, name="delete-appointment"),
    path('addappointment/', addAppointment, name="appointment-add"),
    # path('acceptappointment/', acceptappointment, name="appointment-accept"),
]