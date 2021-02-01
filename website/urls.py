# coding: UTF-8
from django.urls import path

# Import du module views de l'application users
from website import views, cbv

app_name = "website"

urlpatterns = [
    path("", views.defaultView, name="default"),
    path("hello/", views.defaultView, name="default"),
    path("website/list", views.index, name="index"),
    path("website/add", views.addWebsite, name="add"),
    path('website-<website_id>/', views.edit, name="edit"),
    path('new_website/', views.store, name="store"),
    path(
        'delete-<int:pk>/',
        cbv.WebsiteDeleteView.as_view(),
        name="delete"
    ),
]