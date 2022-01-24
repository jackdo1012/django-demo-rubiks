from django.db import models

class Rubiks(models.Model):
    name = models.CharField(max_length=100)
    layers = models.IntegerField()
    brand = models.CharField(max_length=100)
