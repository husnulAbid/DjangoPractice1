from django.shortcuts import render
from rest_framework import generics

from accounts.models import Operations
from .serializers import OperationsSerializer


class OperationsAPIView(generics.ListAPIView):
    queryset = Operations.objects.all()
    serializer_class = OperationsSerializer

# Create your views here.
