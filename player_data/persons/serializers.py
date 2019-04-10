from rest_framework import serializers

from player_data import persons
from player_data.persons.models import Team,Player,Career,Record


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            '球队名',
            '主教练',
            '介绍',
            '进入NBA',
            '场均助攻',
            '场均失分',
            '场均失误',
            '场均得分',
            '场均篮板',
        )


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            # '头像',
            '中文名',
            '位置',
            '体重',
            '合同',
            '国籍',
            '学校',
            '序号',
            '本赛季薪金',
            '球队',
            '生日',
            '英文名',
            '身高',
            '选秀',
            '球队名',
        )

        extra_kwargs = {'学校': {'allow_blank': True,
                               'required': False},
                        '选秀': {'allow_blank': True,
                               'required': False},
                        '国籍': {'allow_blank': True,
                               'required': False},
                        '合同': {'allow_blank': True,
                               'required': False},
                        '英文名': {'allow_blank': True,
                               'required': False},
                        '本赛季薪金': {'allow_blank': True,
                               'required': False},
                        '中文名': {'allow_blank': True,
                               'required': False},

                    }


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = (
            '类型',
            '三分',
            '助攻',
            '命中率',
            '场次',
            '失误',
            '得分',
            '投篮',
            '抢断',
            '时间',
            '犯规',
            '盖帽',
            '篮板',
            '罚球',
            '序号',
        )
class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = (
            '序号',
            '排名',
            '数值',
        )
