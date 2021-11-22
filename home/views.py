from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import *


class SettingView(ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
