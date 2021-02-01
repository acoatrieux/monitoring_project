# coding: UTF-8
from django.urls import path

from urls import views

app_name = 'urls'

urlpatterns = [
	path('hello/', views.hello, name="hello"),
]