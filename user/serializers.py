from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from blog.serializers import BlogSerializer
from .models import *


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, data):
        if data.get('password1') and data.get('password2'):
            if data['password1'] != data['password2']:
                raise serializers.ValidationError('Passwords must match.')
        return data

    def create(self, validated_data):
        print(validated_data)
        data = {
            key: value for key, value in validated_data.items()
            if key not in ('password1', 'password2')
        }
        data['password'] = validated_data['password1']
        data['username'] = validated_data['username']
        user = self.Meta.model.objects.create_user(**data)
        user.is_active = True
        user.save()
        return user

    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'user_permissions', 'groups', 'date_joined', 'first_name', 'last_name']
        read_only_fields = ('last_login', 'is_staff', 'is_superuser', 'is_active')
        write_only_fields = ('password1', 'password2')


class FamousPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamousPeople
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Adminstrator
        fields = ['user', 'first_name', 'last_name']


class TokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user'] = UserSerializer(instance=self.user, context=self.context).data
        return data
