from django.urls import path
from ..views import *

appointmenturl = [
    path('viewappointment/', viewAppointment, name="appointment-view"),
    path('deleteappointment<id>/', deleteAppointment, name="delete-appointment"),
    # path('addappointment/', addAppointment, name="appointment-add"),
    path('addappointmentUser/', addAppointmentUser, name="appointment-add-user"),
    # path('addappointmentUserDoctor/', addAppointmentUserDoctor, name="appointment-add-user-doctor"),
    # path('acceptappointment/', acceptappointment, name="appointment-accept"),
    path('viewuserappointment/', viewAppointment_UserSide, name="user-appointment-view"),
    path('adduserappointment/', addAppointment_UserSide, name="user-appointment-add"),
    path('addUserProfileAppointment/', addAppointment_UserProfile, name="user-profile-appointment-add"),
    

    path('download',download_csv,name='download')

]
