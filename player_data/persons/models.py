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


class Career(models.Model):

    三分 = models.FloatField()
    助攻 = models.FloatField()
    命中率 = models.FloatField()
    场次 = models.FloatField()
    失误 = models.FloatField()
    得分 = models.FloatField()
    投篮 = models.FloatField()
    抢断 = models.FloatField()
    时间 = models.FloatField()
    犯规 = models.FloatField()
    盖帽 = models.FloatField()
    篮板 = models.FloatField()
    罚球 = models.FloatField()
    序号 = models.ForeignKey(to="Player", to_field="序号", on_delete=models.CASCADE)


class Player(models.Model):

    头像 = models.ImageField(upload_to='')
    中文名 = models.CharField(max_length=30)
    位置 = models.CharField(max_length=20)
    体重 = models.CharField(max_length=30)
    合同 = models.CharField(max_length=200)
    国际 = models.CharField(max_length=50)
    学校 = models.CharField(max_length=100)
    序号 = models.CharField(max_length=20, primary_key=True)
    本赛季薪金 = models.CharField(max_length=20)
    球队 = models.CharField(max_length=20)
    生日 = models.CharField(max_length=20)
    英文名 = models.CharField(max_length=20)
    身高 = models.CharField(max_length=20)
    球队名 = models.ForeignKey(to="Team", to_field="球队名", on_delete=models.CASCADE, verbose_name=u"所属球队")




