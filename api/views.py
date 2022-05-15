import json
from django.forms import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer
from products.models import Product

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    # DRF API view 
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)
    