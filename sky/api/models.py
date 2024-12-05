from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField()
    age = models.IntegerField()


