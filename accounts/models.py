from django.db import models

# Create your models here.
class Operations(models.Model):
    type = models.CharField(max_length=100)
    input = models.IntegerField()
    result = models.IntegerField()
