from io import StringIO
import json
import sys
import os

import pymysql
from django.utils.six import BytesIO
pwd = os.path.dirname(os.path.realpath(__file__))
# 获取项目名的目录(因为我的当前文件是在项目名下的文件夹下的文件.所以是../)

sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "软工.settings")
import requests
# 获取当前文件的目录
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


import django
django.setup()
import data_spider
from player_data.persons.models import Player, Team, Record ,Match_teamsummary, Match, Match_player, Score,Schedule
from player_data.persons.serializers import PlayerSerializer, TeamSerializer, RecordSerializer, CareerSerializer,MatchSerializer,Match_playerSerializer,Match_teamsummarySerializer,ScoreSerializer
from django.core.files import File

#
# queryset=Match_teamsummary.objects.all()
#
# for ob in queryset:
#     if ob.主客场=='1':
#         ob.主客场=ob.比赛id.客场球队中文名
#     elif ob.主客场=='2':
#         ob.主客场=ob.比赛id.主场球队中文名
#     ob.save()


queryset=Schedule.objects.all()

for ob in queryset:
    if ob.主客场=='1':
        ob.主客场=ob.比赛id.客场球队中文名
    elif ob.主客场=='2':
        ob.主客场=ob.比赛id.主场球队中文名
    ob.save()
