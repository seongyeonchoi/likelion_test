"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app1.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path('clubs/<int:club_id>/', club_detail_view, name='club_detail'),
    path('clubs/add/', add_club_view, name='add_club'),
    path('clubs/<int:club_id>/edit/', edit_club_view, name='edit_club'),
    path('clubs/<int:club_id>/delete/', delete_club_view, name='delete_club'),
    path('clubs/<int:club_id>/add_comment/', add_comment_view, name='add_comment'),
]
