from rest_framework import serializers

from app_user.operation.models import subscribe


class subscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = subscribe

        fields = (
            'team'
        )
        depth=1