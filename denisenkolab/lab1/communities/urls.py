from django.contrib import admin
from django.urls import path
from . import views

app_name = 'communities'

urlpatterns = [
    path('', views.communities_list, name="list"),
    path('new-post/', views.post_new, name="new-post"),
    path('<slug:slug>', views.communities_page, name="page")
]