from io import StringIO
import json
import sys
import os
from django.utils.six import BytesIO
pwd = os.path.dirname(os.path.realpath(__file__))
# 获取项目名的目录(因为我的当前文件是在项目名下的文件夹下的文件.所以是../)

sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "软工.settings")
# 获取当前文件的目录
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


import django
django.setup()
from player_data.persons.models import Player,Team
from player_data.persons.serializers import PlayerSerializer,TeamSerializer
from django.core.files import File
#接下来就可以使用model了


# with open('./active_players(1).json') as f:
#     active_players = json.load(f)
# active_players = active_players['active_players']
#
# for player in active_players:
#     try:
#         content = JSONRenderer().render(player)
#         stream = BytesIO(content)
#         data = JSONParser().parse(stream)
#         serializer = PlayerSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#         else:
#             print(serializer.errors)
#     except Exception:
#         print(Exception.with_traceback())

with open('./team_config.json') as f:
    team_list= json.load(f)
team_list=team_list['teams']['config']

for team in team_list:
    if team.get('ttsName')!=None:
        image_path="team/"+team.get('tricode')+"_logo.svg"
        image=open(image_path)
        image=File(image)
        team['teamLogo']=image

        content = JSONRenderer().render(team)
        stream = BytesIO(content)
        data = JSONParser().parse(stream)
        #serializer = TeamSerializer(data=data)
        if 1:
            #serializer.save()
            Teamob=Team.objects.get(teamId=team['teamId'])
            Teamob.teamLogo=image
            Teamob.save()
        else:
            print(serializer.errors)