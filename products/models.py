from tokenize import Triple
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null= True)
    price = models.FloatField()

