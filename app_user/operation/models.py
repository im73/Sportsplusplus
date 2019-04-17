from django.db import models
from app_user.user.models import User
from player_data.persons.models import Team
from player_data.persons.serializers import TeamSerializer
# Create your models here.

class subscribe(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    team=models.ForeignKey(Team,on_delete=models.CASCADE)

    class Meta:
        verbose_name=u"关注球队"
        verbose_name_plural=verbose_name