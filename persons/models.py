from django.db import models

# Create your models here.


class Team(models.Model):
    teamname = models.CharField(max_length=50)
    teamLogo = models.ImageField(upload_to='media/image')

    #def __unicode__(self):
    #    return self.teamname


class Player(models.Model):
    collegeName = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    dateOfBirthUTC = models.DateField(auto_now_add=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    heightFeet = models.FloatField(6, 5)
    heightInches = models.FloatField(6, 5)
    heightMeters = models.FloatField(6, 5)
    nbaDebutYear = models.DateField(auto_now_add=True)
    temporaryDisplayName = models.CharField(max_length=50)
    weightKilograms = models.FloatField(6, 5)
    weightPounds = models.FloatField(6, 5)
    playerLogo = models.ImageField(upload_to='media/image')
    #ss

    teamId = models.ForeignKey("Team", on_delete=models.CASCADE)

    #def __unicode__(self):  ss
    #    return u'%s %s' % (self.firstName, self.lastName)


class Career(models.Model):
    season = models.IntegerField(5)
    ppg = models.FloatField(6, 5)
    rpg = models.FloatField(6, 5)
    apg = models.FloatField(6, 5)
    mpg = models.FloatField(6, 5)
    topg = models.FloatField(6, 5)
    spg = models.FloatField(6, 5)
    bpg = models.FloatField(6, 5)
    tpp = models.FloatField(6, 5)
    ftp = models.FloatField(6, 5)
    fgp = models.FloatField(6, 5)
    steals = models.IntegerField(5)
    turnovers = models.IntegerField(5)
    offReb = models.IntegerField(5)
    defReb = models.IntegerField(5)
    totReb = models.IntegerField(5)
    fgm = models.IntegerField(5)
    fga = models.IntegerField(5)
    ftm = models.IntegerField(5)
    fta = models.IntegerField(5)
    pFouls = models.IntegerField(5)
    points = models.IntegerField(5)
    gamesPlayed = models.IntegerField(5)
    gamesStarted = models.IntegerField(5)
    plusMinus = models.IntegerField(5)
    mins = models.IntegerField(5)

    personid = models.ForeignKey("Player", on_delete=models.CASCADE)

    #def __init__(self):
    #   return self.personid



