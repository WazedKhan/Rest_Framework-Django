from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'content', 'price', 'sale_price', 'discount']

    def get_discount(self, obj):
        return obj.get_discount()
        # this method can return info about user and related models data 