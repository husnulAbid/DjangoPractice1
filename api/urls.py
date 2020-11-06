from django.contrib import admin
from django.urls import path, include

from api import views
from api.views import OperationsAPIView
# from api.views import SqAPIView

urlpatterns = [
    path('', OperationsAPIView.as_view()),
    path('input', views.myV),
    path('op=<str:op>&num=<int:number>', views.numberOp)
    #path('sq', SqAPIView.as_view())
]
