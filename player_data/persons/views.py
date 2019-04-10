from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import random

