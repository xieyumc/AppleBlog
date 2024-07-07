from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import WebConfig

def web_config(request):
    config = {item.key: item.value for item in WebConfig.objects.all()}
    return JsonResponse(config)