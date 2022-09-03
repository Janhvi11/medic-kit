"""medic_kit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('reg/', include('register.urls')),
    path('ad/', include('admin_side.urls')),
    path('todo/', include('todo.urls'), name="todo"),
    path('about/', views.about, name="about"),
    path('blog/', views.news, name="blog"),
    path('news/', views.blog, name="news"),
    path('buy/', views.buy, name="buy"),
    path('client/', views.client, name="client"),
    path('contact/', views.contact, name="contact"),
    path('doctors/', views.doctors, name="doctors"),
    path('index/', views.index, name="index")
    # path('login/', include('register.urls')),#
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),#
]