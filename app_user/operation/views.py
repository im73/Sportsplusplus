from urllib import parse

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import json

from app_user.operation.models import subscribe as sb
from app_user.user.models import User
from player_data.persons.models import Team
from app_user.operation.serializer import subscribeSerializer


@csrf_exempt
def Sbscribe(request):

    if request.method=="POST":

        username=request.POST.get('username')
        teamname=request.POST.get('teamname')

        user=User.objects.get(nick_name=username)
        team=Team.objects.get(球队中文名__endswith=teamname)

        sbob=sb(user=user,team=team)
        sbob.save()
        return JsonResponse({'message':'添加关注'}, status=201)

    elif request.method=="GET":

        username=request.GET.get("username")
        user=User.objects.get(nick_name=username)
        sblist=sb.objects.filter(user=user)

        serializer=subscribeSerializer(sblist,many=True)

        return HttpResponse(json.dumps(serializer.data,ensure_ascii=False),content_type="application/json,charset=utf-8",status=200)


    elif request.method=="DELETE":

        username=request.GET.get('username')
        teamname=request.GET.get('teamname')

        user=User.objects.get(nick_name=username)
        team=Team.objects.get(球队中文名__endswith=parse.unquote(teamname))

        sbob=sb.objects.get(user=user,team=team)
        sbob.delete()

        return JsonResponse({'message':'取消关注'}, status=204)

