from os import stat
import grequests
from time import sleep

def get_all_types():


    urls = ['https://pokeapi.co/api/v2/type/'+ str(number) for number in range(1, 19)]
    rs = (grequests.get(u) for u in urls)
    result_json = []

    for response in grequests.map(rs):
        type_dict = {
            'name': '',
            'double_damage_from': [],
            'double_damage_to': [],
            'half_damage_from': [],
            'half_damage_to': [],
            'no_damage_from': [],
            'no_damage_to': []
            }

        type_json = response.json()

        type_dict['name'] = type_json['name']

        for elem in type_json['damage_relations']['double_damage_from']:
            type_dict['double_damage_from'].append(elem['name'])
        
        for elem in type_json['damage_relations']['double_damage_to']:
            type_dict['double_damage_to'].append(elem['name'])
        
        for elem in type_json['damage_relations']['half_damage_from']:
            type_dict['half_damage_from'].append(elem['name'])
        
        for elem in type_json['damage_relations']['half_damage_to']:
            type_dict['half_damage_to'].append(elem['name'])
        
        for elem in type_json['damage_relations']['no_damage_from']:
            type_dict['no_damage_from'].append(elem['name'])
        
        for elem in type_json['damage_relations']['no_damage_to']:
            type_dict['no_damage_to'].append(elem['name'])

        result_json.append(type_dict)
    
    return result_json


def get_all_moves():

    urls = ['https://pokeapi.co/api/v2/move/'+ str(number) for number in range(1, 827)]
    rs = (grequests.get(u) for u in urls)
    result_json = []

    for response in grequests.map(rs):
        move_dict = {
            'name': '',
            'accuracy': '',
            'damage_class': [],
            'power': '',
            }

        move_json = response.json()
        move_dict['name'] = move_json['name']
        move_dict['accuracy'] = move_json['accuracy']
        move_dict['power'] = move_json['power']
        move_dict['damage_class'] = move_json['damage_class']['name']

        result_json.append(move_dict)
    
    return result_json

def get_pokemon_data():
    # name, height, weight, sprite, types, moves, 
    urls = ['https://pokeapi.co/api/v2/pokemon/'+ str(number) for number in range(1, 152)]
    rs = (grequests.get(u) for u in urls)
    result_json = []

    for response in grequests.map(rs):
        poke_dict = {
            'name': '',
            'height': '',
            'weight': '',
            'sprite': '',
            'types': [],
            'stats': [],
            'moves': [],
            }

        poke_json = response.json()
        poke_dict['name'] = poke_json['name']
        poke_dict['height'] = poke_json['height']/10
        poke_dict['sprite'] = poke_json['sprites']['front_default']
        poke_dict['weight'] = poke_json['weight']/10

        for elem in poke_json['types']:
            poke_dict['types'].append(elem['type']['name'])
        
        for elem in poke_json['moves']:
            poke_dict['moves'].append(elem['move']['name'])
        
        stat_dict = {}
        for elem in poke_json['stats']:
            stat_dict[elem['stat']['name']] = elem['base_stat']
            
        poke_dict['stats'].append(stat_dict)

        result_json.append(poke_dict)
    
    return result_json
