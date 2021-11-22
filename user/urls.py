from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('famous-people', FamousPeopleView)
router.register('admin', AdminView)

urlpatterns = [
    path('admin-login/', TokenGenerateView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls)),
]
