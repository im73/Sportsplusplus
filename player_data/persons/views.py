


from urllib import parse


from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.utils import json
import time


from player_data.persons.models import Team, Player, Career, Match, Match_player, Match_teamsummary, Schedule
from player_data.persons.serializers import TeamSerializer, PlayerSerializer, CareerSerializer, MatchSerializer, \
    Match_playerSerializer, Match_teamsummarySerializer, ScheduleSerializer
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

        if request.GET.get('match_id') == "":

            querylist = Match.objects.filter(日期__istartswith=time.strftime("%Y-%m-%d"))
        else :
            querylist = Match.objects.filter(id=request.GET.get('match_id'))
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
def GetPlayerImage(request,PlayerName):

    if request.method == 'GET':
        try:
            image_path=Player.objects.get(中文名=PlayerName.replace(" ","")).头像.path
            image_data = open(image_path,"rb").read()
            return HttpResponse(image_data,content_type='image/jpg')
        except:
            return HttpResponse(json.dumps({'message':'没有获取到资源'},ensure_ascii=False),content_type="application/json,charset=utf-8",status=400)

@csrf_exempt
def GetTeamImage(request,Teamname):

    if request.method == 'GET':
        print(Teamname)
        image_path=Team.objects.get(球队中文名__endswith=parse.unquote(Teamname)).队标.path
        try:
            image_data = open(image_path,"rb").read()
            return HttpResponse(image_data,content_type='image/jpg')
        except:
            return HttpResponse(json.dumps({'message':'没有获取到资源'},ensure_ascii=False),content_type="application/json,charset=utf-8",status=400)
@csrf_exempt
def GetSchedule(request):

    if request.method=="GET":

        teamname=request.GET.get('teamname')
        querylist=Schedule.objects.filter(英文名=teamname)
        serializer=ScheduleSerializer(querylist,many=True)

        return HttpResponse(json.dumps(serializer.data,ensure_ascii=False),content_type="application/json,charset=utf-8",status=200)


