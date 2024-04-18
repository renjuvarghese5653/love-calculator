

from django.db import models

class Name(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    score = models.IntegerField()

