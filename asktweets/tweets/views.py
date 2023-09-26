from rest_framework import viewsets
from django.http import JsonResponse

def json_response(request):
    return JsonResponse({'foot':'bart'})