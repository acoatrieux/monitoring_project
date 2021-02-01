# coding: UTF-8
from django.urls import path

# Import du module views de l'application users
from website import views

app_name = "website"

urlpatterns = [
    path("hello/", views.defaultView, name="default"),
]