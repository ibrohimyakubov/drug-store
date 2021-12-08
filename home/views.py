from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from user.models import Adminstrator
from .serializers import *


class SettingView(ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def setting(request):
    admin = Adminstrator.objects.get(user=request.user)
    setting_ = Setting(user=admin)

    if request.method == 'POST':
        serializer = SettingSerializer(setting_, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def setting_update(request, pk):
    try:
        setting = Setting.objects.get(id=pk)
    except Setting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = SettingSerializer(setting, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Setting has updated successfully'
            return Response(data=data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def setting_delete(request, pk):
    try:
        admin = Adminstrator.objects.get(user=request.user)
        setting = Setting.objects.get(id=pk)
    except Setting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Adminstrator.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        if admin:
            operation = setting.delete()
            data = {}
            if operation:
                data['success'] = 'delete successfully'
            else:
                data['failure'] = 'fail deleted blog'
            return Response(data=data)
        elif admin.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
