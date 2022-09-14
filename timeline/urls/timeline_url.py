from django.urls import path
from ..views import *

time_url = [
    path('viewTimeAdminline/', viewAdminTime, name="view-admin-time"),
    # ============ USER =========================================
    path('viewTimeline/', viewTime, name="view-time"),
    path('editTimeline<id>/', editTime, name="edit-time"),
    path('addTimeline/', addTime, name="add-time"),
    path('deleteTimeline<id>/', deleteTime, name="delete-time"),

    # ============ DOCTOR =========================================
    path('viewTimeline-doc/', viewdocTime, name="view-doc-time"),
    path('editTimeline-doc<id>/', editdocTime, name="edit-doc-time"),
    path('addTimeline-doc/', adddocTime, name="add-doc-time"),
    path('deleteTimeline-doc<id>/', deletedocTime, name="delete-doc-time"),
    
    # ============ PHARMACIST =========================================
    path('viewTimeline-pharma/', viewpharmaTime, name="view-pharma-time"),
    path('editTimeline-pharma<id>/', editpharmaTime, name="edit-pharma-time"),
    path('addTimeline-pharma/', addpharmaTime, name="add-pharma-time"),
    path('deleteTimeline-pharma<id>/', deletepharmaTime, name="delete-pharma-time"),
    
]