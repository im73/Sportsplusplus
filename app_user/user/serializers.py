
from rest_framework import serializers

from app_user.user.models import User,back_user


class UserSerializer(serializers.ModelSerializer):

   class Meta:
       model=User
       fields=('id','email','nick_name','password','image')

class back_userSerialiser(serializers.ModelSerializer):

    class Meta:
        model=back_user
        fields='__all__'






