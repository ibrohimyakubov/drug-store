from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import *


class FamousPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamousPeople
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=50)
    avatar = serializers.ImageField()

    class Meta:
        model = Adminstrator
        fields = ['id', 'first_name', 'last_name', 'phone', 'avatar']


class TokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user'] = AdminSerializer(instance=self.user, context=self.context).data
        return data
