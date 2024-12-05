from django.contrib import admin
from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.communities_list, name="list"),
    path('<slug:slug>', views.community_page, name="page")
]