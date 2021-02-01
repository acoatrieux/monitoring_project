# coding: UTF-8
from django.urls import path

# Import du module views de l'application users
from website import views

app_name = "website"

urlpatterns = [
    path("", views.defaultView, name="default"),
    path("hello/", views.defaultView, name="default"),
    path("website/list", views.index, name="index"),
    path("website/add", views.addWebsite, name="add"),
    path('new_website/', views.store, name="store"),

]