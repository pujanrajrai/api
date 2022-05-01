from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from first_app.models import PictureDesc
from .serializers import PictureDescSerializers


@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        pictures = PictureDesc.objects.all()
        serializer = PictureDescSerializers(pictures, many=True)
        return JsonResponse(serializer.data, safe=False)

