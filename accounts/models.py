from django.db import models


# Create your models here.
class operations(models.Model):
    type = models.CharField(max_length=100)
    input = models.IntegerField()
    result = models.IntegerField()
