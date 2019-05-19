from urllib import parse

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import json

from app_user.operation.models import subscribe as sb
from app_user.user.models import User,tokens
from player_data.persons.models import Team
from app_user.operation.serializer import subscribeSerializer
from app_user.mymatch.models import Subscribe,MyGame


@csrf_exempt
def Sbscribe(request):

    if request.method == "POST":


        username=request.POST.get('username')
        teamname=request.POST.get('teamname')

        user=User.objects.get(nick_name=username)
        team=Team.objects.get(球队中文名__endswith=teamname)

        sbob=sb(user=user,team=team)
        sbob.save()

        return JsonResponse({'message':'添加关注'}, status=201)

    elif request.method == "GET":


        username=request.GET.get("username")
        user=User.objects.get(nick_name=username)
        sblist=sb.objects.filter(user=user)

        serializer=subscribeSerializer(sblist,many=True)

        return HttpResponse(json.dumps(serializer.data,ensure_ascii=False),content_type="application/json,charset=utf-8",status=200)

    elif request.method == "DELETE":


        username=request.GET.get('username')
        teamname=request.GET.get('teamname')

        user=User.objects.get(nick_name=username)
        team=Team.objects.get(球队中文名__endswith=parse.unquote(teamname))

        sbob=sb.objects.get(user=user,team=team)
        sbob.delete()

        return JsonResponse({'message':'取消关注'}, status=204)


@csrf_exempt
def Validate(request):

    if request.method == "POST":

        data = json.loads(request.body)

        if data.get("method") == "user":

            user = User.objects.filter(nick_name=data.get("username"))

            if user.count()==0:
                return JsonResponse({'message':'用户不存在'}, status=400)
            else:
                return JsonResponse({'message':'用户存在'}, status=200)

        if data.get("method") == "team":

            username = data.get("username")
            teamname = data.get("teamname")

            user=User.objects.get(nick_name=username)
            team=Team.objects.get(球队中文名__endswith=teamname)

            sbob=sb.objects.filter(user=user,team=team)

            if sbob.count()==0:
                return JsonResponse({'message':'未关注球队'}, status=400)
            else:
                return JsonResponse({'message':'已关注球队'}, status=200)

        if data.get("method") == "schedule":

            scheduleid = data.get('scheduleid')
            username = data.get('username')

            user = User.objects.get(nick_name=username)
            sublist = MyGame.objects.get(id=scheduleid)

            sbob = Subscribe.objects.filter(赛程=sublist,用户=user)

            if sbob.count()==0:
                return JsonResponse({'message':'未关注赛程'}, status=400)
            else:
                return JsonResponse({'message':'已关注赛程'}, status=200)





