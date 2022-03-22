import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from covid.models import Covid
from rest_framework.response import Response
from rest_framework.decorators import api_view
from covid.serializer import CovidSerializer
@api_view(["POST"])
def api_home(request,*args,**kwargs):
    """DRF API VIEW"""
    
    serializer = CovidSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        #instance = serializer.save()
        #print(instance)
        return Response(serializer.data)
    return Response("Not good Data")