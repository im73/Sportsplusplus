# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Team(models.Model):

    teamId =models.CharField(max_length=20,primary_key=True,null=False,verbose_name=u"队伍编号")
    ttsName = models.CharField(max_length=50,verbose_name=u"队伍名",default="")
    teamLogo = models.ImageField(upload_to='',verbose_name=u"队伍图标")
    primaryColor = models.CharField(max_length=10)
    secondaryColor = models.CharField(max_length=10)
    #def __unicode__(self):
    #    return self.teamname
    class Meta:
        verbose_name = u"球队"
        verbose_name_plural = verbose_name


class Player(models.Model):

    personId = models.CharField(max_length=20,primary_key=True)
    collegeName = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    dateOfBirthUTC = models.DateField(auto_now_add=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    heightFeet = models.FloatField()
    heightInches = models.FloatField()
    heightMeters = models.FloatField()
    nbaDebutYear = models.DateField(auto_now_add=True)
    temporaryDisplayName = models.CharField(max_length=50)
    weightKilograms = models.FloatField()
    weightPounds = models.FloatField(verbose_name=u"")
    playerLogo = models.ImageField(upload_to='',verbose_name=u"球员头像",null=True)
    teamId = models.ForeignKey(to="Team",to_field="teamId", on_delete=models.CASCADE,verbose_name=u"所属球队")

    class Meta:

        verbose_name = u"球员"
        verbose_name_plural = verbose_name




class Career(models.Model):

    season = models.IntegerField()
    ppg = models.FloatField()
    rpg = models.FloatField()
    apg = models.FloatField()
    mpg = models.FloatField()
    topg = models.FloatField()
    spg = models.FloatField()
    bpg = models.FloatField()
    tpp = models.FloatField()
    ftp = models.FloatField()
    fgp = models.FloatField()
    steals = models.IntegerField()
    turnovers = models.IntegerField()
    offReb = models.IntegerField()
    defReb = models.IntegerField()
    totReb = models.IntegerField()
    fgm = models.IntegerField()
    fga = models.IntegerField()
    ftm = models.IntegerField()
    fta = models.IntegerField()
    pFouls = models.IntegerField()
    points = models.IntegerField()
    gamesPlayed = models.IntegerField()
    gamesStarted = models.IntegerField()
    plusMinus = models.IntegerField()
    mins = models.IntegerField()
    personId = models.ForeignKey(to="Player",to_field="personId", on_delete=models.CASCADE,verbose_name=u"所属球员")

    class Meta:
        verbose_name = u"职业生涯"
        verbose_name_plural = verbose_name

    #def __init__(self):
    #   return self.personid



