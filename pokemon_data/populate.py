import grequests
import requests
from django.core.files import File
from pokemon_data.img_processing import get_sprite
from random import choice
from pokemon_data.fetch_content import get_all_moves, get_all_types, get_pokemon_data
from pokemon_data.models import ModelsPokemon, Type, Move

def populate_moves():
    json = get_all_moves()

    for each_move in json:
        new_move_args = {
            'name':each_move['name'],
            'accuracy':each_move['accuracy'],
            'power':each_move['power'],
            'damage_class':each_move['damage_class']
        }
        if not bool(new_move_args['power']):
            new_move_args['power'] = 0
        if not (new_move_args['accuracy']):
            new_move_args['accuracy'] = 0

        new_move = Move(
            name=each_move['name'],
            accuracy=each_move['accuracy'],
            power=each_move['power'],
            damage_class=each_move['damage_class']
            )
        new_move.save()
    
    return 'completed'

def populate_types():
    json = get_all_types()

    for each_move in json:

        new_move = Type(
            name=each_move['name'],
            double_damage_from={'double_damage_from':each_move['double_damage_from']},
            double_damage_to={'double_damage_to':each_move['double_damage_to']},
            half_damage_from={'half_damage_from':each_move['half_damage_from']},
            half_damage_to={'half_damage_to':each_move['half_damage_to']},
            no_damage_from={'no_damage_from':each_move['no_damage_from']},
            no_damage_to={'no_damage_to':each_move['no_damage_to']},
            )
        new_move.save()
    
    return 'completed'

def populate_pokemons():
    json = get_pokemon_data()

    for each_type in json:
        new_pokemon_args = {
            'name':each_type['name'],
            'height':each_type['height'],
            'weight':each_type['weight'],
            'sprite':each_type['sprite'],            
            'types':each_type['types'],
            'move_set':each_type['moves'],
            'stats': each_type['stats'][0]
        }
        

        for stat in new_pokemon_args['stats']:
            new_pokemon_args[stat] = new_pokemon_args['stats'][stat]
        
        img_data = get_sprite(each_type['name'], each_type['sprite'])

        if len(new_pokemon_args['types']) > 1:
            new_pokemon_args['type_1'] = new_pokemon_args['types'][0]
            new_pokemon_args['type_2'] = new_pokemon_args['types'][1]
        else:
            new_pokemon_args['type_1'] = new_pokemon_args['types'][0]
        
        new_pokemon_args['move'] = choice(new_pokemon_args['move_set'])

        if "type_2" in new_pokemon_args:
            new_pokemon = ModelsPokemon(
                name=new_pokemon_args['name'],
                height=new_pokemon_args['height'],
                weight=new_pokemon_args['weight'],
                type_1=Type.objects.all().filter(name=new_pokemon_args['type_1'])[0],
                type_2=Type.objects.all().filter(name=new_pokemon_args['type_2'])[0],
                move_set={'move_set':new_pokemon_args['move_set']},
                move=new_pokemon_args['move'],
                hp=new_pokemon_args['hp'],
                attack=new_pokemon_args['attack'],
                defense=new_pokemon_args['defense'],
                special_attack=new_pokemon_args['special-attack'],
                special_defense=new_pokemon_args['special-defense'],
                speed=new_pokemon_args['speed']            
            )
        else:
            new_pokemon = ModelsPokemon(
                name=new_pokemon_args['name'],
                height=new_pokemon_args['height'],
                weight=new_pokemon_args['weight'],
                type_1=Type.objects.all().filter(name=new_pokemon_args['type_1'])[0],
                move_set={'move_set':new_pokemon_args['move_set']},
                move=new_pokemon_args['move'],
                hp=new_pokemon_args['hp'],
                attack=new_pokemon_args['attack'],
                defense=new_pokemon_args['defense'],
                special_attack=new_pokemon_args['special-attack'],
                special_defense=new_pokemon_args['special-defense'],
                speed=new_pokemon_args['speed']
                )
        
        new_pokemon.sprite.save(str(new_pokemon_args['name'])+'.jpg', File(open('pokemon_data/static/pokemon/'+str(new_pokemon_args['name'])+'.jpg', 'rb')))
    print(new_pokemon_args)

    return new_pokemon_args
    
populate_types()
populate_moves()
populate_pokemons()