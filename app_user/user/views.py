from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from app_user.user.models import User,email_very,back_user
from app_user.user.serializers import UserSerializer
import random
from api.send_email import get_random_str
from django.core.mail import send_mail, send_mass_mail

from 软工 import settings


@csrf_exempt
def register(request):
    """
    user register by ph_number.
    """
    if request.method == 'GET':
        email=request.GET.get('email')
        verification_code=random.randrange(100000,999999)
        email_from = settings.DEFAULT_FROM_EMAIL
        tmp = loader.get_template('active.html')
        htm_email = tmp.render({"msg":str(verification_code)})
        msg = ""
        title = 'Sports++验证码'
        reciever = [email]
        emailob = email_very.objects.filter(email=email)
        if emailob.count()!=0:
            emailob.first().delete()
        print(email)
        emailob=email_very(email=email,very_code=verification_code,op_type=1) #1是注册
        emailob.save()

        send_mail(title, msg, email_from, reciever, html_message=htm_email)
        return JsonResponse({'message':'success'}, status=200)

    elif request.method == 'POST':

        nick_name=request.POST.get('nick_name')
        password=request.POST.get('password')
        email=request.POST.get('email')
        verification_code=request.POST.get('veri_code')

        try:
            emailob=email_very.objects.get(email=email)
            if emailob.very_code!=verification_code:
                return JsonResponse({'err_code':'验证码错误'}, status=400)
            user=User(nick_name=nick_name,password=password,email=email)
            user.save()
            emailob.delete()

            return JsonResponse({'message':'success'}, status=201)
        except Exception:
            print(Exception)
            return JsonResponse({'message':'用户已存在'}, status=400)

@csrf_exempt
def login(request):
    """
    user login by ph_number.
    """
    if request.method == 'GET':
        nick_name=request.GET.get('nick_name')
        password=request.GET.get('password')
        user=User.objects.filter(nick_name=nick_name,password=password)
        if user.count()==0:
            return JsonResponse({'message':'用户名或密码错误'}, status=400)
        else:
            return JsonResponse({'message':'登录成功'}, status=200)


@csrf_exempt
def back_login(request):
    """
    user login by ph_number.
    """
    if request.method == 'GET':
        nick_name=request.GET.get('nick_name')
        password=request.GET.get('password')
        user=back_user.objects.filter(nick_name=nick_name,password=password)
        if user.count()==0:
            return JsonResponse({'message':'用户名或密码错误'}, status=400)
        else:
            return JsonResponse({'message':'登录成功'}, status=200)
