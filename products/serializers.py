from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'content', 'price', 'sale_price', 'get_discount']
