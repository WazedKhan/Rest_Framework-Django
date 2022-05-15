import json
from django.forms import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    # DRF API view 
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id','title','price','sale_price']) # fields = ['id','title'] used to specify which fields to sent by default sent all the fields
    return Response(data)
    