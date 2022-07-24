from pokemon_data.fetch_content import get_all_moves, get_all_types, get_pokemon_data
from pokemon_data.models import Pokemon, Type, Move

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

    for each_type in json:

        new_type = Type(
            name=each_type['name'],
            double_damage_from={'double_damage_from':each_type['double_damage_from']},
            double_damage_to={'double_damage_to':each_type['double_damage_to']},
            half_damage_from={'half_damage_from':each_type['half_damage_from']},
            half_damage_to={'half_damage_to':each_type['half_damage_to']},
            no_damage_from={'no_damage_from':each_type['no_damage_from']},
            no_damage_to={'no_damage_to':each_type['no_damage_to']},
            )
        new_type.save()
    
    return 'completed'

# def populate_pokemons():
#     json = get_pokemon_data()

#     for each_type in json:

#         new_type = Type(
#             name=each_type['name'],
#             double_damage_from={'double_damage_from':each_type['double_damage_from']},
#             double_damage_to={'double_damage_to':each_type['double_damage_to']},
#             half_damage_from={'half_damage_from':each_type['half_damage_from']},
#             half_damage_to={'half_damage_to':each_type['half_damage_to']},
#             no_damage_from={'no_damage_from':each_type['no_damage_from']},
#             no_damage_to={'no_damage_to':each_type['no_damage_to']},
#             )
#         new_type.save()
    
#     return 'completed'
