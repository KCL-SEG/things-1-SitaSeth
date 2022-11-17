from django.db import models

# Create your models here.
class Thing(models.Model): #extends django.db.models.Model
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    quantity = models.IntegerField()
    