import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
# 获取项目名的目录(因为我的当前文件是在项目名下的文件夹下的文件.所以是../)

sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "软工.settings")
# 获取当前文件的目录


import django
django.setup()
from player_data.persons.models import Match

#
# queryset=Match_teamsummary.objects.all()
#
# for ob in queryset:
#     if ob.主客场=='1':
#         ob.主客场=ob.比赛id.客场球队中文名
#     elif ob.主客场=='2':
#         ob.主客场=ob.比赛id.主场球队中文名
#     ob.save()


# queryset=Schedule.objects.all()
#
# for ob in queryset:
#     if ob.主客场=='1':
#         ob.主客场=ob.比赛id.客场球队中文名
#     elif ob.主客场=='2':
#         ob.主客场=ob.比赛id.主场球队中文名
#     ob.save()
import random
import math
queryset=Match.objects.filter()
for ob in queryset:
    ob.胜率=math.floor(random.random()*25)+45
    ob.save()
