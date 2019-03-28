
from rest_framework import serializers

from app_user.user.models import User


class UserSerializer(serializers.Serializer):

    id=serializers.IntegerField(read_only=True)
    ph_number=serializers.CharField(max_length=11,allow_blank=False,required=True)
    nick_name=serializers.CharField(max_length=12,allow_blank=False,required=True)
    register_time=serializers.DateTimeField()
    image=serializers.ImageField(allow_empty_file=True)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.ph_number = validated_data.get('ph_number', instance.ph_number)
        instance.nick_name = validated_data.get('nick_name', instance.nick_name)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        return instance






