from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from . import models

def all_mobiles(request: HttpRequest):
    if request.method == 'GET':
        mobiles = list(models.Mobile.objects.all().values())
        return JsonResponse(mobiles, safe=False)
    return JsonResponse({'error': 'Please use GET method to get all mobiles.'})
