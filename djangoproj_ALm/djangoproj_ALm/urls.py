
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('mission/', views.mission , name="mission"),
    path('vision/', views.vision, name = "vision"),
    path('objectives/', views.objectives, name = "objectives")
     
]
