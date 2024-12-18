import uuid
from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class Bunga (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255) #CharField ada batasan input
    price = models.IntegerField()
    description = models.TextField()
    stocks = models.IntegerField()
    img_url = models.URLField()