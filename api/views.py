import json
from django.shortcuts import render
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) #json.load converts json data into python dictionary
    except:
        pass
    print(data)
    return JsonResponse(data)