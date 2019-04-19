
from rest_framework import serializers

from app_user.user.models import User,back_user


class UserSerializer(serializers.ModelSerializer):
    register_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    class Meta:
        model=User
        fields=('id','email','nick_name','password','register_time')

class back_userSerializer(serializers.ModelSerializer):
    addtime = serializers.DateTimeField(format="%Y-%m-%d ", required=False)
    class Meta:
        model=back_user
        exclude = ('password',)






