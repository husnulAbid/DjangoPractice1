from rest_framework import serializers
from accounts.models import Operations


class OperationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operations
        fields = '__all__'