


from urllib import parse
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.utils import json


from player_data.persons.models import Team,Player,Career,Match,Match_teamsummary,Match_player
from player_data.persons.serializers import TeamSerializer,PlayerSerializer,CareerSerializer,MatchSerializer,Match_teamsummarySerializer,Match_playerSerializer
import random


@csrf_exempt
def get_teaminfo(request):

    if request.method == 'GET':

        teamlist=Team.objects.all()
        serializer = TeamSerializer(teamlist,many=True)
        return HttpResponse(json.dumps(serializer.data,ensure_ascii=False),content_type="application/json,charset=utf-8",status=200)

@csrf_exempt
def get_playerinfo(request):

    if request.method == 'GET':

        team_name=request.GET.get('teamname')
        Playerlist=Player.objects.filter(球队名=team_name)
        serializer=PlayerSerializer(Playerlist,many=True)

        return HttpResponse(json.dumps(serializer.data,ensure_ascii=False),content_type="application/json,charset=utf-8",status=200)

@csrf_exempt
def get_playercareer(request):

    if request.method == 'GET':

        player_index=request.GET.get('player_index')
        careerlist=Career.objects.filter(序号=player_index)
        serializer=CareerSerializer(careerlist,many=True)

        return HttpResponse(json.dumps(serializer.data,ensure_ascii=False),content_type="application/json,charset=utf-8",status=200)

@csrf_exempt
def GetMatchInfo(request):

    if request.method == 'GET':
        querylist = Match.objects.all()
        serializer=MatchSerializer(querylist,many=True)
        return HttpResponse(json.dumps(serializer.data,ensure_ascii=False),content_type="application/json,charset=utf-8",status=200)
@csrf_exempt
def GetMatchSummary(request):

    if request.method == 'GET':
        match_id=request.GET.get('match_id')
        querylist = Match_teamsummary.objects.filter(比赛id=match_id)
        serializer=Match_teamsummarySerializer(querylist,many=True)
        return HttpResponse(json.dumps(serializer.data,ensure_ascii=False),content_type="application/json,charset=utf-8",status=200)

@csrf_exempt
def GetPlayerSummary(request):

    if request.method == 'GET':
        match_id=request.GET.get('match_id')
        querylist = Match_player.objects.filter(比赛id=match_id)
        serializer=Match_playerSerializer(querylist,many=True)
        return HttpResponse(json.dumps(serializer.data,ensure_ascii=False),content_type="application/json,charset=utf-8",status=200)


@csrf_exempt
def GetPlayerImage(request,path):

    if request.method == 'GET':
        image_path="media/player_profile_json/{0}/portrait.png".format(parse.unquote(path,encoding ='utf-8').encode('utf8'))
        print(image_path)
        try:
            image_data = open(image_path,"rb").read()
            return HttpResponse(image_data,content_type='image/jpg')
        except:
            return HttpResponse(json.dumps({'message':'没有获取到资源'},ensure_ascii=False),content_type="application/json,charset=utf-8",status=400)

@csrf_exempt
def GetTeamImage(request,path):

    if request.method == 'GET':
        print(path)
        image_path="media/teams_img/{0}".format(parse.unquote(path,encoding="utf8"))
        print(image_path)
        try:
            image_data = open(image_path,"rb").read()
            return HttpResponse(image_data,content_type='image/jpg')
        except:
            return HttpResponse(json.dumps({'message':'没有获取到资源'},ensure_ascii=False),content_type="application/json,charset=utf-8",status=400)
