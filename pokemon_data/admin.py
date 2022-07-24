from django.contrib import admin
from .models import ModelsPokemon, Type, Move

admin.site.register(ModelsPokemon)
admin.site.register(Type)
admin.site.register(Move)