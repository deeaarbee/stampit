from django.shortcuts import render
from django.db.models import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from backend.manager import RequestManager
from backend.base import send_response
from django.views.generic.base import View
from backend.functions import composed
from django.db import IntegrityError


# Test API #############################################################################################################
class TestAPI(APIView):
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)

    @staticmethod
    def get(request):
        return send_response(data={"hello": "World"}, status=200)


