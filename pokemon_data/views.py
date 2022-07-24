from django.shortcuts import render
from .models import Type, Move, ModelsPokemon
from .serializer import TypeSerializer, MoveSerializer, ModelsPokemonSerializer
from rest_framework import viewsets

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class MoveViewSet(viewsets.ModelViewSet):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer

class ModelsPokemonViewSet(viewsets.ModelViewSet):
    queryset = ModelsPokemon.objects.all()
    serializer_class = ModelsPokemonSerializer