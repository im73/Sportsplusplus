from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from app_user.user.models import User
from app_user.user.serializers import UserSerializer
import random

@csrf_exempt
def register(request):
    """
    user register by ph_number.
    """
    if request.method == 'GET':
        ph_number=request.GET.get('ph_number')
        verification_code=random.randrange(100000,999999)
        return JsonResponse({'veri_code':verification_code}, status=200)
    elif request.method == 'POST':
        nick_name=request.POST.get('nick_name')
        ph_number=request.POST.get('ph_number')
        try:
            UserSerializer.create(nick_name=nick_name,ph_number=ph_number)
            return JsonResponse({'message':'success'}, status=201)
        except Exception:
            print(Exception)
            return JsonResponse({'err_code':''}, status=400)

@csrf_exempt
def login(request):
    """
    user login by ph_number.
    """
    if request.method == 'GET':
        ph_number=request.GET.get('ph_number')
        verification_code=random.randrange(100000,999999)
        return JsonResponse({'veri_code':verification_code}, status=200)
    elif request.method == 'POST':
        ph_number=request.POST.get('ph_number')
        try:
            user=User.objects.get(ph_number=ph_number)
            if user:
                return JsonResponse({'message':'success'}, status=201)
            else :
                return JsonResponse({'message':'fail'}, status=401)
        except Exception:
            print(Exception)
            return JsonResponse({'err_code':''}, status=401)
