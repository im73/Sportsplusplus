from rest_framework import serializers

from player_data import persons
from player_data.persons.models import Team,Player,Career


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('teamId', 'ttsName','primaryColor','secondaryColor')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            'personId',
            'country',
            'dateOfBirthUTC',
            'firstName',
            'lastName',
            'heightFeet',
            'heightInches',
            'heightMeters',
            'collegeName',
            'nbaDebutYear',
            'teamId',
            'temporaryDisplayName',
            'weightKilograms',
            'playerLogo',
            'weightPounds',
        )

class Career(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = (
            'personid',
            'season',
            'ppg',
            'rpg',
            'apg',
            'mpg',
            'topg',
            'spg',
            'bpg',
            'tpp',
            'ftp',
            'fgp',
            'steals',
            'turnovers',
            'offReb',
            'defReb',
            'totReb',
            'fgm',
            'fga',
            'ftm',
            'fta',
            'pFouls',
            'points',
            'gamesPlayed',
            'gamesStarted',
            'plusMinus',
            'min',
        )
