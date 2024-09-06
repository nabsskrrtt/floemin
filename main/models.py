from django.db import models

# Create your models here.
class Bunga (models.Model):
    name = models.CharField(max_length=255) #CharField ada batasan input
    price = models.IntegerField()
    description = models.TextField()