from rest_framework import routers, serializers, viewsets
from .views import TypeViewSet, MoveViewSet, ModelsPokemonViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'types', TypeViewSet)
router.register(r'moves', MoveViewSet)
router.register(r'pokemons', ModelsPokemonViewSet)


urlpatterns = [
    path('', include(router.urls))
]