# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Team(models.Model):

    teamId = models.CharField(max_length=20, primary_key=True,null=False, verbose_name=u"队伍编号")
    ttsName = models.CharField(max_length=50, verbose_name=u"队伍名", default="")
    teamLogo = models.ImageField(upload_to='', verbose_name=u"队伍图标")
    primaryColor = models.CharField(max_length=10, verbose_name=u"主色")
    secondaryColor = models.CharField(max_length=10, verbose_name=u"辅色")

    class Meta:
        verbose_name = u"球队"
        verbose_name_plural = verbose_name


class Player(models.Model):

    personId = models.CharField(max_length=20, primary_key=True,verbose_name=u"个人id")
    collegeName = models.CharField(max_length=50, verbose_name=u"大学名字")
    country = models.CharField(max_length=50, verbose_name=u"国家")
    dateOfBirthUTC = models.DateField(auto_now_add=True, verbose_name=u"出生日期")
    firstName = models.CharField(max_length=20, verbose_name=u"名")
    lastName = models.CharField(max_length=20, verbose_name=u"姓")
    heightFeet = models.FloatField()
    heightInches = models.FloatField(verbose_name=u"身高-英尺")
    heightMeters = models.FloatField(verbose_name=u"身高-米")
    nbaDebutYear = models.DateField(auto_now_add=True)
    temporaryDisplayName = models.CharField(max_length=50, verbose_name=u"别名")
    weightKilograms = models.FloatField(verbose_name=u"体重-千克")
    weightPounds = models.FloatField(verbose_name=u"体重-磅")
    playerLogo = models.ImageField(upload_to='', verbose_name=u"球员头像", null=True)
    teamId = models.ForeignKey(to="Team", to_field="teamId", on_delete=models.CASCADE, verbose_name=u"所属球队")

    class Meta:

        verbose_name = u"球员"
        verbose_name_plural = verbose_name


class Career(models.Model):

    season = models.IntegerField(verbose_name=u"赛季")
    ppg = models.FloatField(verbose_name=u"场均得分数")
    rpg = models.FloatField(verbose_name=u"场均篮板数")
    apg = models.FloatField(verbose_name=u"场均助攻数")
    mpg = models.FloatField(verbose_name=u"场均上长时间数")
    topg = models.FloatField(verbose_name=u"场均失误次数")
    spg = models.FloatField(verbose_name=u"场均抢断数")
    bpg = models.FloatField(verbose_name=u"场均封盖数")
    tpp = models.FloatField(verbose_name=u"三分命中率")
    ftp = models.FloatField(verbose_name=u"罚球命中率")
    fgp = models.FloatField(verbose_name=u"投篮命中率")
    steals = models.IntegerField(verbose_name=u"总抢断数")
    turnovers = models.IntegerField(verbose_name=u"总失误数")
    offReb = models.IntegerField(verbose_name=u"前场篮板数")
    defReb = models.IntegerField(verbose_name=u"后场篮板数")
    totReb = models.IntegerField(verbose_name=u"总篮板数")
    fgm = models.IntegerField(verbose_name=u"投篮进球数")
    fga = models.IntegerField(verbose_name=u"投篮出手数")
    ftm = models.IntegerField(verbose_name=u"罚球命中数")
    fta = models.IntegerField(verbose_name=u"罚球出手数")
    pFouls = models.IntegerField(verbose_name=u"总犯规数")
    points = models.IntegerField(verbose_name=u"总得分数")
    gamesPlayed = models.IntegerField(verbose_name=u"参与场次数")
    gamesStarted = models.IntegerField(verbose_name=u"首发次数")
    plusMinus = models.IntegerField(verbose_name=u"总正负值")
    mins = models.IntegerField(verbose_name=u"总上场时长（单位分钟）")
    personId = models.ForeignKey(to="Player",to_field="personId", on_delete=models.CASCADE,verbose_name=u"所属球员")

    class Meta:
        verbose_name = u"职业生涯"
        verbose_name_plural = verbose_name



