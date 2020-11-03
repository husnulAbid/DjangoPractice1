from django.contrib import admin
from django.urls import path, include

from api.views import OperationsAPIView

urlpatterns = [
    path('', OperationsAPIView.as_view()),
]
