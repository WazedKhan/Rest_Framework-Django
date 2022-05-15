import json
from turtle import title
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse

from products.models import Product

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data) # fields = ['id','title'] used to specify which fields to sent by default sent all the fields
    return JsonResponse(data)
    