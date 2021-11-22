from drf_yasg import openapi
from django.shortcuts import render
from rest_framework import status as rest_status
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import *


class FamousPeopleView(ModelViewSet):
    queryset = FamousPeople.objects.all()
    serializer_class = FamousPeopleSerializer


class AdminView(ModelViewSet):
    serializer_class = AdminSerializer
    queryset = Adminstrator.objects.all()
    permission_classes = (permissions.AllowAny,)

    def get_serializer_context(self):
        return {'request': self.request}


class TokenGenerateView(TokenObtainPairView):
    serializer_class = TokenSerializer
    post_responses = {
        rest_status.HTTP_201_CREATED: openapi.Response(description='Token obtained'),
        rest_status.HTTP_404_NOT_FOUND: openapi.Response(description='User not found'),
        rest_status.HTTP_400_BAD_REQUEST: openapi.Response(description='Validation error'),
    }

    def get_serializer_context(self):
        return {'request': self.request}
