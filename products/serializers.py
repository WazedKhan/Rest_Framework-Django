from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'content', 'price', 'sale_price', 'discount']

    def get_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None
        # this method can return info about user and related models data 