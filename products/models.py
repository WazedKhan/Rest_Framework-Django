from tokenize import Triple
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null= True)
    price = models.FloatField()

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)

    def get_discount(self):
        return 212