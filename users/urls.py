from rest_framework import routers, serializers, viewsets
from .views import UserViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'data', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]