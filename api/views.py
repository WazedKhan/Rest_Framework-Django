import json
from django.shortcuts import render
from django.http import JsonResponse

def api_home(request, *args, **kwargs):

    print(request.GET)
    print(request.POST)
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) #json.load converts json data into python dictionary
    except:
        pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    return JsonResponse(data)