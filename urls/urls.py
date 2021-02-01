# coding: UTF-8
from django.urls import path

from users import views, cbv

app_name = 'urls'
urlpatterns = [
    path('hello/', views.hello, name="hello"),
]