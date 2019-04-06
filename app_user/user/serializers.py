
from rest_framework import serializers

from app_user.user.models import User


class UserSerializer(serializers.ModelSerializer):

   class Meta:
       field=('email','nick_name','password')






