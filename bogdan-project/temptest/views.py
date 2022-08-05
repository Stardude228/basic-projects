import json
from pprint import pprint
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from django.contrib.auth import get_user_model
# from .templates import cars

User = get_user_model()

class TemplateView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        user = list(User.objects.values())
        return Response({'user': user[0]})

@api_view(["GET"])
def get_users(request):
    return Response([*User.objects.values()])