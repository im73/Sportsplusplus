from django.db import models

# Create your models here.

from app_user.user.models import User


class MyGame(models.Model):

    创建者 = models.ForeignKey(User,on_delete=models.CASCADE)
    名称 = models.CharField(max_length=40)
    简介 = models.CharField(max_length=300)
    时间 = models.CharField(max_length=40)
    创建时间 = models.DateTimeField(auto_now_add=True,verbose_name=u"创建时间")


class GameManager(models.Model):

    赛程 = models.ForeignKey(MyGame,on_delete=models.CASCADE)
    管理员 = models.ForeignKey(User,on_delete=models.CASCADE)


class MyMatch(models.Model):

    赛程 = models.ForeignKey(MyGame,on_delete=models.CASCADE)
    日期 = models.CharField(max_length=20)
    时间 = models.CharField(max_length=20)
    地点 = models.CharField(max_length=40)
    主场 = models.CharField(max_length=40)
    客场 = models.CharField(max_length=40)

    主场第一节 = models.CharField(max_length=10,default='0')
    主场第二节 = models.CharField(max_length=10,default='0')
    主场第三节 = models.CharField(max_length=10,default='0')
    主场第四节 = models.CharField(max_length=10,default='0')
    主场加时1 = models.CharField(max_length=10,default='0')
    主场加时2 = models.CharField(max_length=10,default='0')
    主场加时3 = models.CharField(max_length=10,default='0')
    主场加时4 = models.CharField(max_length=10,default='0')

    客场第一节 = models.CharField(max_length=10,default='0')
    客场第二节 = models.CharField(max_length=10,default='0')
    客场第三节 = models.CharField(max_length=10,default='0')
    客场第四节 = models.CharField(max_length=10,default='0')
    客场加时1 = models.CharField(max_length=10,default='0')
    客场加时2 = models.CharField(max_length=10,default='0')
    客场加时3 = models.CharField(max_length=10,default='0')
    客场加时4 = models.CharField(max_length=10,default='0')

    主场总分 = models.CharField(max_length=10,default='0')
    客场总分 = models.CharField(max_length=10,default='0')

    加时场数 = models.IntegerField(default=0)

class GamePlayer(models.Model):

    比赛 = models.ForeignKey(MyMatch,on_delete=models.CASCADE)
    球队名 = models.CharField(max_length=40)
    球员名 = models.CharField(max_length=40)
    位置 = models.CharField(max_length=10)
    得分 = models.CharField(max_length=10)
    篮板 = models.CharField(max_length=10)
    助攻 = models.CharField(max_length=10)
    三分 = models.CharField(max_length=10)
    罚球 = models.CharField(max_length=10)
    抢断 = models.CharField(max_length=10)
    助攻 = models.CharField(max_length=10)
    失误 = models.CharField(max_length=10)
    号码 = models.CharField(max_length=10)

class Subscribe(models.Model):

    用户 = models.ForeignKey(User,on_delete=models.CASCADE,related_name="关注者")
    赛程 = models.ForeignKey(MyGame,on_delete=models.CASCADE)

