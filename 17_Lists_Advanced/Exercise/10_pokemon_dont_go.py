available_pokemons = [int(x) for x in input().split()]

total_pokemons = 0

while len(available_pokemons) > 0:
    catch_pokemon = int(input())

    dynamic_value = 0
    if catch_pokemon > len(available_pokemons) - 1:
        catch_pokemon = len(available_pokemons) - 1
        dynamic_value += available_pokemons[catch_pokemon]
        available_pokemons.pop(catch_pokemon)
        available_pokemons.append(available_pokemons[0])
    elif catch_pokemon < 0:
        catch_pokemon = 0
        dynamic_value += available_pokemons[0]
        available_pokemons.pop(0)
        available_pokemons.insert(0, available_pokemons[-1])
    else:
        dynamic_value += available_pokemons[catch_pokemon]
        available_pokemons.pop(catch_pokemon)
    for element in range(0, len(available_pokemons)):
        if available_pokemons[element] > dynamic_value:
            available_pokemons[element] -= dynamic_value
        elif available_pokemons[element] <= dynamic_value:
            available_pokemons[element] += dynamic_value
    total_pokemons += dynamic_value

print(total_pokemons)


# list_of_positions = [int(ch) for ch in input().split()]
#
# total_pokemons = 0
#
# while len(list_of_positions) > 0:
#     index = int(input())
#
#     current_number = 0
#     if index > len(list_of_positions) - 1:
#         index = len(list_of_positions) - 1
#         current_number += list_of_positions[index]
#         del list_of_positions[index]
#         list_of_positions.append(list_of_positions[0])
#     elif index < 0:
#         index = 0
#         current_number += list_of_positions[0]
#         del list_of_positions[0]
#         list_of_positions.insert(0, list_of_positions[-1])
#     else:
#         current_number += list_of_positions[index]
#         del list_of_positions[index]
#
#     for i in range(0, len(list_of_positions)):
#         if list_of_positions[i] > current_number:
#             list_of_positions[i] -= current_number
#         elif list_of_positions[i] <= current_number:
#             list_of_positions[i] += current_number
#
#     total_pokemons += current_number
#
# print(total_pokemons)