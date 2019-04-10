from io import StringIO
import json
import sys
import os
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
from player_data.persons.models import Player,Team,Record
from player_data.persons.serializers import PlayerSerializer,TeamSerializer,RecordSerializer
from django.core.files import File
#接下来就可以使用model了

#添加球员信息
# with open('./active_players(1).json') as f:
#     active_players = json.load(f)
# active_players = active_players['active_players']
#
# for player in active_players:
#     try:
#         if (player.get('personId')!=None)&(Player.objects.filter(personId=player.get('personId')).count()==0):
#             image_path="player/"+player.get('personId')+".png"
#             try:
#                 image=open(image_path,'rb')
#             except:
#                 image=open("player/0000.png",'rb')
#             image=File(image)
#             content = JSONRenderer().render(player)
#             stream = BytesIO(content)
#             data = JSONParser().parse(stream)
#             serializer = PlayerSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 playerob=Player.objects.get(personId=player.get('personId'))
#                 playerob.playerLogo=image
#                 playerob.save()
#             else:
#                 print(serializer.errors)
#     except Exception:
#         print(Exception.with_traceback())
# #添加球队
# with open('./team_config.json') as f:
#     team_list= json.load(f)
# team_list=team_list['teams']['config']
#
# for team in team_list:
#     if team.get('ttsName')!=None:
#         image_path="team/"+team.get('tricode')+"_logo.svg"
#         image=open(image_path)
#         image=File(image)
#
#         content = JSONRenderer().render(team)
#         stream = BytesIO(content)
#         data = JSONParser().parse(stream)
#         #serializer = TeamSerializer(data=data)
#         if 1:
#             #serializer.save()
#             Teamob=Team.objects.get(teamId=team['teamId'])
#             Teamob.teamLogo=image
#             Teamob.save()
#         else:
#             print(serializer.errors)

# glg = data_spider.GetLiveGames()
# # glg.get_scores()
# # glg.get_active_players()
# # glg.get_schedule()
# # glg.get_player_profile()
# with open('./active_players(1).json') as f:
#     active_players = json.load(f)
# active_players = active_players['active_players']
# # profile = {}
# for player in active_players:
#     if (player.get('personId')!=None):
#         player_profile = requests.get(glg.player_profile.format(player['personId'])).json()
#     # profile[player['personId']] = player_profile
#         player_profile = json.dumps(player_profile, sort_keys=True, indent=8, separators=(',', ':'))
#         career_total=player_profile['league']['standard']['stats']['careerSummary']


import os

file_dir="./team_info"
team_index=0
index=0
for root, dirs, files in os.walk(file_dir):
    print(files) #当前路径下所有非目录子文件
    for file in files:
        with open(root+"/"+file) as f:
            team_info = json.load(f)
        print(team_info)
        team_info=team_info[file.split('.')[0]]
        team_info['球队名']=file.split('.')[0]
        info=team_info['技术统计']
        for item in info:
            item_info=info[str(item)]
            item_info['序号']=index
            index=index+1
            if Record.objects.filter(序号=index).count()!=0:
                continue
            content = JSONRenderer().render(item_info)
            stream = BytesIO(content)
            data = JSONParser().parse(stream)
            serializer = RecordSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)

        team_info['场均助攻']=str(team_index*5+0)
        team_info['场均失分']=str(team_index*5+1)
        team_info['场均失误']=str(team_index*5+2)
        team_info['场均得分']=str(team_index*5+3)
        team_info['场均篮板']=str(team_index*5+4)

        content = JSONRenderer().render(team_info)
        stream = BytesIO(content)
        data = JSONParser().parse(stream)
        serializer = TeamSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        team_index=team_index+1
