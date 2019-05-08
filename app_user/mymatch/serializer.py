from rest_framework import serializers

from app_user.mymatch.models import MyMatch,GameManager,GamePlayer,MyGame,Subscribe


class MyMatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyMatch
        fields = '__all__'



class GameManagerSerializer(serializers.ModelSerializer):

    class Meta:

        model = GameManager
        fields = ( '赛程' ,)
        depth = 1

class MyGameSerializer(serializers.ModelSerializer):

    class Meta:

        model = MyGame
        fields = '__all__'

class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Subscribe
        fields = ('赛程',)
        depth=1


class GamePLayerSerializer(serializers.ModelSerializer):

    class Meta:

        model = GamePlayer
        fields = '__all__'
