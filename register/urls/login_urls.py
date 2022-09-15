from django.urls import path
from ..views import *

login_url = [
    path('login/', login_home, name='login-home'),
    path('loginuser/', login_request, name='user-login'),
    path('logindoctor/', login_doc_request, name='doc-login'),
    path('loginpharma/', login_pharma_request, name='pharma-login'),
    path('logout/', logout, name='logout'),
    
    # profile
    path('userProfile/',userprofile, name="user-profile")
]

# redirect_authenticated_user=True, 