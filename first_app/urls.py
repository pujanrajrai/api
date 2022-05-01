from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('get/photo/details', views.snippet_list, name='get_photo'),
]
