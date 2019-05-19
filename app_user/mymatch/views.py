import io
from io import BytesIO

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.utils import json
from django.http import QueryDict
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from app_user.mymatch.models import MyGame,GameManager,MyMatch,GamePlayer,Subscribe
from app_user.user.models import User
from app_user.mymatch.serializer import GameManagerSerializer,MyMatchSerializer,MyGameSerializer,SubscribeSerializer,GamePLayerSerializer
# from api.Querytodict import request_body_serialze
from json import loads, dumps
from api.PUTapi import PUThandle

@csrf_exempt
def myschedule(request):

    if request.method=="POST":

        username = request.POST.get('username')
        time = request.POST.get('time')
        name = request.POST.get('name')
        intro = request.POST.get('introduction')
        manager = request.POST.get('manager')
        managerlist = manager.split('+')

        user = User.objects.get(nick_name=username)

        game=MyGame(创建者=user,名称=name,简介=intro,时间=time)
        game.save()

        GameManager(赛程=game,管理员=user).save()
        for username in managerlist:
            user = User.objects.get(nick_name=username)
            GameManager(赛程=game,管理员=user).save()

        return JsonResponse({'message':'添加成功','schedule_id':'{}'.format(game.id)}, status=201)

    if request.method=="GET":

        username = request.GET.get('username')
        user = User.objects.get(nick_name=username)

        gamelist=GameManager.objects.filter(管理员=user)

        serializer=GameManagerSerializer(gamelist,many=True)

        return HttpResponse(json.dumps(serializer.data,ensure_ascii=False),content_type="application/json,charset=utf-8",status=200)

    if request.method == "DELETE":


        data = json.loads(request.body)

        try:
            scheduleob = MyGame.objects.get(id=data.get("scheduleid"))
        except:
            return JsonResponse({'message':'赛程不存在'}, status=400)
        scheduleob.delete()

        return JsonResponse({'message':'删除成功'}, status=204)




@csrf_exempt
def mymatch(request):

    if request.method=="GET":

        gameid = request.GET.get('gameid')

        game = MyGame.objects.get(id=gameid)
        matchlist = MyMatch.objects.filter(赛程=game)

        serializer=MyMatchSerializer(matchlist,many=True)

        return HttpResponse(json.dumps(serializer.data,ensure_ascii=False),content_type="application/json,charset=utf-8",status=200)

    if request.method=="POST":

        gameid = request.POST.get('gameid')
        game=MyGame.objects.get(id=gameid)

        time = request.POST.get('time')
        date = request.POST.get('date')
        location =request.POST.get('location')
        home = request.POST.get('home')
        away = request.POST.get('away')

        MyMatch(赛程=game,时间=time,日期=date,地点=location,主场=home,客场=away).save()
        return JsonResponse({'message':'创建比赛成功','match_id':'{}'.format()}, status=201)

    if request.method == "PUT":


        data = json.loads(request.body)

        matchid = data.get('matchid')


        match=MyMatch.objects.get(id=matchid)

        home1 = data.get('home1')
        home2 = data.get('home2')
        home3 = data.get('home3')
        home4 = data.get('home4')
        home5 = data.get('home5')
        home6 = data.get('home6')
        home7 = data.get('home7')
        home8 = data.get('home8')

        away1 = data.get('away1')
        away2 = data.get('away2')
        away3 = data.get('away3')
        away4 = data.get('away4')
        away5 = data.get('away5')
        away6 = data.get('away6')
        away7 = data.get('away7')
        away8 = data.get('away8')

        OT = data.get('OT')

        total_home = data.get('home_total')
        total_away = data.get('away_total')

        match.主场第一节 = home1
        match.主场第二节 = home2
        match.主场第三节 = home3
        match.主场第四节 = home4
        match.主场加时1 = home5
        match.主场加时2 = home6
        match.主场加时3 = home7
        match.主场加时4 = home8

        match.客场第一节 = away1
        match.客场第二节 = away2
        match.客场第三节 = away3
        match.客场第四节 = away4
        match.客场加时1 = away5
        match.客场加时2 = away6
        match.客场加时3 = away7
        match.客场加时4 = away8

        match.主场总分 = total_home
        match.客场总分 = total_away

        match.加时场数 = int(OT)

        match.save()

        return JsonResponse({'message':'比赛数据修改成功'}, status=200)


@csrf_exempt
def player(request):

    if request.method=="POST":

        matchid = request.POST.get('matchid')
        match=MyMatch.objects.get(id=matchid)

        teamname = request.POST.get('teamname')
        playername = request.POST.get('playername')
        position =request.POST.get('position')

        GamePlayer(球队名=teamname,球员名=playername,比赛=match,位置=position).save()

        return JsonResponse({'message':'添加球员成功'}, status=201)

    if request.method=="PUT":

        playerlist=json.loads(request.body)

        for item in playerlist:

            ply = GamePlayer.objects.get(id=item.get("id"))
            ply.得分 = item.get("得分")
            ply.篮板 = item.get("篮板")
            ply.助攻 = item.get("助攻")
            ply.三分 = item.get("三分")
            ply.罚球 = item.get("罚球")
            ply.抢断 = item.get("抢断")
            ply.助攻 = item.get("助攻")
            ply.失误 = item.get("失误")
            ply.号码 = item.get("号码")

            ply.save()

        return JsonResponse({'message':'球员数据修改成功'}, status=200)


    if request.method=="GET":

        scheduleid = request.GET.get('matchid')
        match = MyMatch.objects.get(id=scheduleid)

        playerlist = GamePlayer.objects.filter(比赛=match)

        serializer =  GamePLayerSerializer(playerlist,many=True)

        return HttpResponse(json.dumps(serializer.data,ensure_ascii=False),content_type="application/json,charset=utf-8",status=200)


@csrf_exempt
def AllSchedule(request):

    if request.method=="GET":

        schedulelist = MyGame.objects.all()

        serializer = MyGameSerializer(schedulelist,many=True)

        return HttpResponse(json.dumps(serializer.data,ensure_ascii=False),content_type="application/json,charset=utf-8",status=200)

    if request.method=="POST":

        print(request.body)
        scheduleid = request.POST.get('scheduleid')
        username = request.POST.get('username')

        user = User.objects.get(nick_name=username)
        sublist=MyGame.objects.get(id=scheduleid)

        Subscribe(赛程=sublist,用户=user).save()

        return JsonResponse({'message':'关注赛程成功'}, status=201)


@csrf_exempt
def Subforgame(request):

    if request.method=="POST":

        scheduleid = request.POST.get('scheduleid')
        username = request.POST.get('username')

        user = User.objects.get(nick_name=username)
        sublist = MyGame.objects.get(id=scheduleid)

        Subscribe.objects.get(赛程=sublist,用户=user).delete()

        return JsonResponse({'message':'取消关注'}, status=204)

    if request.method=="GET":

        username = request.GET.get('username')

        user = User.objects.get(nick_name=username)
        schedulelist = Subscribe.objects.filter(用户=user)

        serializer =  SubscribeSerializer(schedulelist,many=True)

        return HttpResponse(json.dumps(serializer.data,ensure_ascii=False),content_type="application/json,charset=utf-8",status=200)










