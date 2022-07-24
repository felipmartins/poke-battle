from .models import ModelsPokemon, Type, Move
from rest_framework import serializers

class MoveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Move
        fields = '__all__'

class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class ModelsPokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelsPokemon
        fields = '__all__'