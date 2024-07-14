from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from . import models
import json
from django.views.decorators.csrf import csrf_exempt


def all_mobiles(request: HttpRequest):
    if request.method == 'GET':
        mobiles = list(models.Mobile.objects.all().values())
        return JsonResponse(mobiles, safe=False)
    return JsonResponse({'error': 'Please use GET method to get all mobiles.'})

def get_mobile(request: HttpRequest, id):
    if request.method == 'GET':
        try:
            mobile = models.Mobile.objects.values().get(pk=id)
            return JsonResponse(mobile, safe=False)

        except models.Mobile.DoesNotExist:
            return JsonResponse({'error': 'this object does not exist'})
    return JsonResponse({'error': 'Please use GET method to get this mobile data.'})

@csrf_exempt
def add_new_mobile(request: HttpRequest):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_mobile = models.Mobile(
                title = data['title'],
                price = data['price'],
                rating = data['rating'],
                brand = data['brand'],
                dimensions_height = data['dimensions_height'],
                dimensions_width = data['dimensions_width'],
                dimensions_thickness = data['dimensions_thickness'],
                weight = data['weight'],
                body_structure = data['body_structure'],
                sim_card_size = data['sim_card_size'],
                sim_card_number = data['sim_card_number'],
                chip = data['chip'],
                cpu_type = data['cpu_type'],
                cpu_frequency = data['cpu_frequency'],
                memory_card_support = data['memory_card_support'],
                screen_technology = data['screen_technology'],
                screen_size = data['screen_size'],
                screen_resolution = data['screen_resolution'],
                supporting_the_1G = data['supporting_the_1G'],
                supporting_the_2G = data['supporting_the_2G'],
                supporting_the_3G = data['supporting_the_3G'],
                supporting_the_4G = data['supporting_the_4G'],
                supporting_the_5G = data['supporting_the_5G'],
                wifi_is_supported = data['wifi_is_supported'],
                bluetooth_is_supported = data['bluetooth_is_supported'],
                gps_is_supported = data['gps_is_supported'],
                camera_resolution = data['camera_resolution'],
                os = data['os'],
            )
            new_mobile.save()
            return JsonResponse({'message': 'mobile added successfully!'})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
    return JsonResponse({'error': 'Please use POST method to add a mobile.'})

@csrf_exempt
def edit_book(request, id):
    if request.method == 'PATCH':
        try:
            mobile = models.Mobile.objects.get(pk=id)
            data = json.loads(request.body)
            for key in data.keys():
                if key not in models.Mobile._meta.fields:
                    return JsonResponse({'error': 'this field does not exist and its value cannot be edited'})
            mobile.__dict__.update(data)
            mobile.save()
            return JsonResponse({'message': 'mobile updated successfully!'})
        
        except models.Mobile.DoesNotExist:
            return JsonResponse({'error': 'this object does not exist'})
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
    return JsonResponse({'error': 'Please use PATCH method to update a mobile.'})