import json
from cmath import sqrt

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import Operations
from .serializers import OperationsSerializer
from . import serializers
from rest_framework.views import APIView


class OperationsAPIView(APIView):
    def get(self, request):
        operation = Operations.objects.all()
        serializer = OperationsSerializer(operation, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def numberOp(request, number, op):
    buttonType = op

    if buttonType == 'double':
        result = number + number
    elif buttonType == 'sq':
        result = number*number

    return Response({'result': result}, status=status.HTTP_201_CREATED)


def myV(request):
    return render(request, 'inputApiSq.html')
