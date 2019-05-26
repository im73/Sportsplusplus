# Create your views here.

# Create your views here.
import datetime
from urllib import parse

from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import json

from app_user.user.models import User,email_very,back_user,tokens,Active
from app_user.user.serializers import UserSerializer,back_userSerializer
import random
import os
from django.core.mail import send_mail
import uuid
from 软工 import settings
import time


@csrf_exempt
def register(request):
    """
    user register by ph_number.
    """

    if request.method == 'GET':

        email=request.GET.get('email')
        if User.objects.filter(email=email).count() !=0:
            return JsonResponse({'message':'already_exists'}, status=200)
        verification_code=random.randrange(100000,999999)
        # verification_code=666666
        email_from = settings.DEFAULT_FROM_EMAIL
        tmp = loader.get_template('active.html')
        htm_email = tmp.render({"msg":str(verification_code)})
        with open("log.txt","w+") as f:
            f.write(email)
        msg = ""
        title = 'Sports++验证码'
        reciever = [email]
        emailob = email_very.objects.filter(email=email)
        if emailob.count()!=0:
            emailob.first().delete()

        emailob=email_very(email=email,very_code=str(verification_code),op_type=1) #1是注册
        emailob.save()

        send_mail(title, msg, email_from, reciever, html_message=htm_email)

        return JsonResponse({'message':'发送成功'}, status=200)

    elif request.method == 'POST':

        nick_name=request.POST.get('nick_name')
        password=request.POST.get('password')
        email=request.POST.get('email')
        verification_code=request.POST.get('veri_code')
        token = uuid.uuid4()
        try:
            emailob=email_very.objects.get(email=email)
            with open("log.txt","a+") as f:
                f.write(emailob.very_code)
                f.write(verification_code)
            if emailob.very_code!=verification_code:
                return JsonResponse({'err_code':'验证码错误'}, status=400)
            user=User(nick_name=nick_name,password=password,email=email)
            user.save()

            tkob=tokens(user=user,active=1,cookie=token)
            tkob.save()

            emailob.delete()
            response =  JsonResponse({'message':'success'}, status=201)
            response.set_cookie("user",token)
            return response

        except Exception:
            print(Exception)
            return JsonResponse({'message':'用户已存在'}, status=400)
    with open("log.txt","w+") as f:
        f.write("没有匹配到方法")

@csrf_exempt
def login(request):
    """
    user login by ph_number.
    """
    if request.method == 'GET':

        token = uuid.uuid4()
        cook=request.COOKIES.get("user")

        if cook:
            print(cook)

        nick_name=request.GET.get('nick_name')
        password=request.GET.get('password')
        user=User.objects.filter(nick_name=nick_name,password=password)

        response =  JsonResponse({'message':'登录成功'}, status=200)
        response.set_cookie("user",token)



        if user.count()==0:
            return JsonResponse({'message':'用户名或密码错误'}, status=400)
        else:
            if tokens.objects.filter(user=user.first()).count()==0:

                tkob=tokens(user=user.first(),active=1,cookie=token)
                tkob.save()
            else:

                tkob=tokens.objects.get(user=user.first())
                tkob.cookie=token
                tkob.active=1
                tkob.save()

            return response


@csrf_exempt
def back_login(request):
    """
    user login by ph_number.
    """
    if request.method == 'GET':
        nick_name=request.GET.get('nick_name')
        password=request.GET.get('password')
        user=back_user.objects.filter(username=nick_name,password=password)
        if user.count()==0:
            return JsonResponse({'message':'用户名或密码错误'}, status=400)
        else:
            return JsonResponse({'message':'登录成功'}, status=200)

@csrf_exempt
def users(request):

    if request.method == 'GET':

        queryset=User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return JsonResponse(serializer.data,safe=False)


    if request.method == 'DELETE':

        id=request.GET.get('id')
        bkob=User.objects.get(id=id)
        bkob.delete()
        return JsonResponse({'message':'用户删除'}, status=204)

        # except :
        #     return JsonResponse({'message':'用户不存在'}, status=400)
    if request.method == 'PUT':
        try:
            print(request.body)
            id = request.GET.get('id')
            email = request.GET.get('email')
            nick_name = request.GET.get('nick_name')
            user=User.objects.get(id=id)
            user.email=email
            user.nick_name=nick_name
            user.save()
            return JsonResponse({'message':'修改成功'}, status=200)
        except:
            return JsonResponse({'message':'修改失败'}, status=400)

@csrf_exempt
def BackUser(request):

    if request.method == 'GET':

        queryset=back_user.objects.all()
        serializer = back_userSerializer(queryset, many=True)
        return JsonResponse(serializer.data,safe=False)

    if request.method == 'POST':

        username=request.GET.get('username')
        password=request.GET.get('password')
        phnumber=request.GET.get('phnumber')
        truename=request.GET.get('truename')


        backuser=back_user(username=username,password=password,phnumber=phnumber,truename=truename)

        try:
            backuser.save()
            serializer = back_userSerializer(backuser)
            return JsonResponse(serializer.data,safe=False,status=201)
        except:
            return JsonResponse({'message':'用户名重复'}, status=400)

    if request.method == 'DELETE':


        try:
            id=request.GET.get('userid')
            bkob=back_user.objects.get(id=id)
            bkob.delete()
            return JsonResponse({'message':'用户删除'}, status=204)
        except :
            return JsonResponse({'message':'用户不存在'}, status=400)

    if request.method == 'PUT':

        userid=request.GET.get('userid')
        username=request.GET.get('username')
        password=request.GET.get('password')
        phnumber=request.GET.get('phnumber')
        truename=request.GET.get('truename')

        Backuser=back_user.objects.get(id=userid)

        Backuser.username=username
        if password!="":
            Backuser.password=password
        Backuser.phnumber=phnumber
        Backuser.truename=truename
        Backuser.addtime=Backuser.addtime
        print(Backuser.addtime)
        try:
            Backuser.save()
            return JsonResponse({'message':'用户信息修改成功'}, status=200)
        except:
            return JsonResponse({'message':'用户名重复'}, status=400)


@csrf_exempt
def GetUserImage(request,path):

    if request.method == 'GET':
        image_path="media/teams_img/{0}".format(parse.unquote(path,encoding="utf8"))
        try:
            image_data = open(image_path,"rb").read()
            return HttpResponse(image_data,content_type='image/jpg')
        except:
            return HttpResponse(json.dumps({'message':'没有获取到资源'},ensure_ascii=False),content_type="application/json,charset=utf-8",status=400)



@csrf_exempt
def GetMatchInfo(request):

    if request.method == 'GET':
        return HttpResponse(json.dumps({'message':'没有获取到资源'},ensure_ascii=False),content_type="application/json,charset=utf-8",status=400)

@csrf_exempt
def Changepassword(request):

    if request.method=='PUT':


        username=request.GET.get('username')
        oldpassword=request.GET.get('old')
        new=request.GET.get('new')

        userob=User.objects.get(nick_name=username)
        if userob.password==oldpassword:
            userob.password=new
            userob.save()
            return HttpResponse(json.dumps({'message':'密码修改成功'},ensure_ascii=False),content_type="application/json,charset=utf-8",status=200)

        else:
            return HttpResponse(json.dumps({'message':'原密码输入错误'},ensure_ascii=False),content_type="application/json,charset=utf-8",status=400)

@csrf_exempt
def BackHome(request):

    if request.method=="GET":

        time=datetime.datetime.now()
        begin_date=(time-datetime.timedelta(days=6)).strftime("%Y-%m-%d")
        end_date=time.strftime("%Y-%m-%d")
        dates = []
        dt = datetime.datetime.strptime(begin_date, '%Y-%m-%d')
        date = begin_date
        while date <= end_date:
            dates.append(date)
            dt = dt + datetime.timedelta(1)
            date = dt.strftime('%Y-%m-%d')
        newnum=[]
        totalnum=[]
        tknum=[]

        for i in range(len(dates)-1):
            newnum.append(User.objects.filter(register_time__range=(dates[i],dates[i+1])).count())
            totalnum.append(User.objects.filter(register_time__lte=dates[i+1]).count())
            if i<(len(dates)-2):
                aclist=Active.objects.filter(date__range=(dates[i+1],dates[i+2]))
            else:
                aclist=Active.objects.filter(date__gte=dates[-1])
            if aclist.count()==0:
                tknum.append(0)
            else:
                tknum.append(aclist.first().num)
        tknum.append(tokens.objects.filter(active=1).count())
        newnum.append(User.objects.filter(register_time__gte=dates[-1]).count())
        totalnum.append(User.objects.all().count())

        data={"tknum":tknum,"newnum":newnum,"totalnum":totalnum,"dates":dates}

        return HttpResponse(json.dumps(data,ensure_ascii=False),content_type="application/json,charset=utf-8",status=200)







