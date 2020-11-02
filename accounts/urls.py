from django.contrib import admin
from django.urls import path

from accounts import views

urlpatterns = [
    path('index', views.index, name = 'index'),
    path('', views.index, name = 'index'),
]
