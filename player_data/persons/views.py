from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.utils import json

from player_data.persons.models import Team
from player_data.persons.serializers import TeamSerializer
import random


@csrf_exempt
def get_teaminfo(request):
    teamob=Team.objects.all().first()
    serializer = TeamSerializer(teamob)
    return HttpResponse(json.dumps(serializer.data,ensure_ascii=False),content_type="application/json,charset=utf-8",status=200)
