from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('singlepage', views.singlepage, name="singlepage"),
    path("", views.index, name="index"),
    path("sections/<int:num>", views.section, name="section")
]
