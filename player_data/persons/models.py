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


class Match_player(models.Model):

    类型 = models.CharField(max_length=10) # 1 首发， 2 替补
    主客场 = models.CharField(max_length=50) # 1 客场， 2 主场
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
    比赛id = models.ForeignKey(to="Match", to_field="id", on_delete=models.CASCADE, default="")


class Match_teamsummary(models.Model):

    主客场 = models.CharField(max_length=50) # 1 客场， 2 主场
    比赛id = models.ForeignKey(to="Match", to_field="id", on_delete=models.CASCADE, default="")
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
    投篮命中率 = models.CharField(max_length=10)
    三分命中率 = models.CharField(max_length=10)
    罚球命中率 = models.CharField(max_length=10)
    home_away = models.IntegerField()


class Score(models.Model):
    第一节 = models.IntegerField()
    第二节 = models.IntegerField()
    第三节 = models.IntegerField()
    第四节 = models.IntegerField()
    总分 = models.IntegerField()


class Match(models.Model):

    id = models.CharField(max_length=10, primary_key=True)
    日期 = models.CharField(max_length=20)
    主场球队中文名 = models.CharField(max_length=20)
    客场球队中文名 = models.CharField(max_length=20)
    主场第一节 = models.CharField(max_length=10)
    主场第二节 = models.CharField(max_length=10)
    主场第三节 = models.CharField(max_length=10)
    主场第四节 = models.CharField(max_length=10)
    主场加时一 = models.CharField(max_length=10)
    主场加时二 = models.CharField(max_length=10)
    主场加时三 = models.CharField(max_length=10)
    主场加时四 = models.CharField(max_length=10)
    客场加时一 = models.CharField(max_length=10)
    客场加时二 = models.CharField(max_length=10)
    客场加时三 = models.CharField(max_length=10)
    客场加时四 = models.CharField(max_length=10)
    主场总分 = models.CharField(max_length=10)
    客场第一节 = models.CharField(max_length=10)
    客场第二节 = models.CharField(max_length=10)
    客场第三节 = models.CharField(max_length=10)
    客场第四节 = models.CharField(max_length=10)
    客场总分 = models.CharField(max_length=10)

    状态 = models.IntegerField(default=1)
    时间 = models.CharField(max_length=20,default="")

    胜率 = models.IntegerField(default=0)

    class Meta:
        ordering = ['日期']




class Schedule(models.Model):

    英文名 = models.CharField(max_length=50)
    赛季球队 = models.CharField(max_length=50)
    主队 = models.CharField(max_length=50)
    客队 = models.CharField(max_length=50)
    主队比分 = models.CharField(max_length=10)
    客队比分 = models.CharField(max_length=10)
    结果 = models.CharField(max_length=10)
    日期 = models.CharField(max_length=20)
    北京时间 = models.CharField(max_length=20)
    类型 = models.CharField(max_length=10) # 数据统计or预测
    比赛id = models.ForeignKey(to="Match", to_field="id", on_delete=models.CASCADE, default="", null=True)

# for i in range(1, 21):
#     setattr(Match, '替补%d' % i, models.ForeignKey(MatchPlayer, on_delete=models.CASCADE, related_name="替补%d信息" % i))
# for j in range(1, 5):
#     setattr(Match, '首发%d' % i, models.ForeignKey(MatchPlayer, on_delete=models.CASCADE, related_name="首发%d信息" % i))

