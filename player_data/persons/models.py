# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Record(models.Model):

    序号 = models.IntegerField(primary_key=True)
    排名 = models.IntegerField()
    数值 = models.FloatField()


class Team(models.Model):

    球队名 = models.CharField(max_length=20, primary_key=True, null=False)
    主教练 =  models.CharField(max_length=20)
    介绍 = models.CharField(max_length=300,  default="")
    队标 = models.ImageField(upload_to='')
    场均助攻 = models.ForeignKey(Record, on_delete=models.CASCADE,related_name="助攻信息")
    场均失分 = models.ForeignKey(Record, on_delete=models.CASCADE,related_name="失分信息")
    场均失误 = models.ForeignKey(Record, on_delete=models.CASCADE,related_name="失误信息")
    场均得分 = models.ForeignKey(Record, on_delete=models.CASCADE,related_name="得分信息")
    场均篮板 = models.ForeignKey(Record, on_delete=models.CASCADE,related_name="篮板信息")
    进入NBA = models.CharField(max_length=20)
    球队中文名 = models.CharField(max_length=20)


class Career(models.Model):

    类型 = models.IntegerField()
    三分 = models.CharField(max_length=20)
    助攻 = models.CharField(max_length=20)
    命中率 = models.CharField(max_length=20)
    场次 = models.CharField(max_length=20)
    失误 = models.CharField(max_length=20)
    得分 = models.CharField(max_length=20)
    投篮 = models.CharField(max_length=20)
    抢断 = models.CharField(max_length=20)
    时间 = models.CharField(max_length=20)
    犯规 = models.CharField(max_length=20)
    盖帽 = models.CharField(max_length=20)
    篮板 = models.CharField(max_length=20)
    罚球 = models.CharField(max_length=20)
    序号 = models.ForeignKey(to="Player", to_field="序号", on_delete=models.CASCADE,default="")


class Player(models.Model):

    头像 = models.ImageField(upload_to='')
    中文名 = models.CharField(max_length=30)
    位置 = models.CharField(max_length=20)
    体重 = models.CharField(max_length=30)
    合同 = models.CharField(max_length=200)
    国籍 = models.CharField(max_length=50)
    学校 = models.CharField(max_length=100)
    序号 = models.CharField(max_length=20, primary_key=True)
    本赛季薪金 = models.CharField(max_length=20)
    球队 = models.CharField(max_length=20)
    生日 = models.CharField(max_length=20)
    英文名 = models.CharField(max_length=50)
    身高 = models.CharField(max_length=20)
    选秀 = models.CharField(max_length=30)
    球队名 = models.ForeignKey(to="Team", to_field="球队名", on_delete=models.CASCADE,default="")


class MatchPlayer(models.Model):

    球员名 = models.CharField(max_length=30)
    位置 = models.CharField(max_length=10)
    时间 = models.CharField(max_length=10)
    投篮 = models.CharField(max_length=10)
    三分 = models.CharField(max_length=10)
    罚球 = models.CharField(max_length=10)
    前场 = models.CharField(max_length=10)
    后场 = models.CharField(max_length=10)
    篮板 = models.CharField(max_length=10)
    助攻 = models.CharField(max_length=10)
    犯规 = models.CharField(max_length=10)
    抢断 = models.CharField(max_length=10)
    失误 = models.CharField(max_length=10)
    封盖 = models.CharField(max_length=10)
    得分 = models.CharField(max_length=10)
    正负 = models.CharField(max_length=10)


class Match(models.Model):

    统计 = models.ForeignKey(MatchPlayer, on_delete=models.CASCADE, related_name="统计信息")
    命中率 = models.ForeignKey(MatchPlayer, on_delete=models.CASCADE, related_name="命中率信息")


for i in range(1, 21):
    setattr(Match, '替补%d' % i, models.ForeignKey(MatchPlayer, on_delete=models.CASCADE, related_name="替补%d信息" % i))
for j in range(1, 5):
    setattr(Match, '首发%d' % i, models.ForeignKey(MatchPlayer, on_delete=models.CASCADE, related_name="首发%d信息" % i))

