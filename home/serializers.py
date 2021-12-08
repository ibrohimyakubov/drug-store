from rest_framework import serializers
from .models import *


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        exclude = ['user']
