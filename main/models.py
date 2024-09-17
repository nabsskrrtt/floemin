import uuid
from django.db import models

# Create your models here.
class Bunga (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255) #CharField ada batasan input
    price = models.IntegerField()
    description = models.TextField()