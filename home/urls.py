from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import *

router = DefaultRouter()
router.register('setting', SettingView)

urlpatterns = [
    path('', include(router.urls)),
    path('add/', views.setting, name='setting'),
    path('update/<int:pk>/', views.setting_update, name='setting-update'),
    path('delete/<int:pk>/', views.setting_delete, name='setting-delete'),
]
