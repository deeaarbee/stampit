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
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)

    @staticmethod
    def get(request):
        return send_response(data={"hello": "World"}, status=200)

# Test API #############################################################################################################


class GetAllCode(APIView):
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)

    @staticmethod
    def get(request):
        data = composed.get_all_html()
        return send_response(data={"data": data}, status=200)


class AddCode(APIView):
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)

    @staticmethod
    def post(request):
        manager = RequestManager()
        data = manager.set_request(request=request).add_html_code()
        return send_response(data=data, status=200)


class AddCount(APIView):
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)

    @staticmethod
    def get(request, unique_code):
        data = composed.increment_count(unique_code=unique_code)
        return send_response(data={"status": data}, status=200)


class DeleteCode(APIView):
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)

    @staticmethod
    def get(request, unique_code):
        data = composed.delete_code(unique_code=unique_code)
        return send_response(data={"status": data}, status=200)


class ChangeStatus(APIView):
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)

    @staticmethod
    def get(request, unique_code):
        data = composed.change_status(unique_code=unique_code)
        return send_response(data={"status": data}, status=200)


class ViewSingleCode(APIView):
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)

    @staticmethod
    def get(request, unique_code):
        data = composed.get_single_code(unique_code=unique_code)
        return send_response(data={"data": data}, status=200)
