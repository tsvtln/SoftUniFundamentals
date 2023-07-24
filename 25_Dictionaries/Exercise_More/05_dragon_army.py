data_dragons = dict()
number_of_dragons_to_follow = int(input())

for stats_of_dragon in range(number_of_dragons_to_follow):
    receive_data = input().split()
    type, name, damage, health, armor = receive_data[0], receive_data[1], receive_data[2], receive_data[3], \
        receive_data[4]
    if damage != 'null':
        damage = int(damage)
    else:
        damage = 45
    if health != 'null':
        health = int(health)
    else:
        health = 250
    if armor != 'null':
        armor = int(armor)
    else:
        armor = 10
    if type not in data_dragons:
        data_dragons[type] = {name: [damage, health, armor]}
    else:
        data_dragons[type][name] = [damage, health, armor]

for color_dragon, name_dragon in data_dragons.items():
    sorted_names = sorted(name_dragon.keys())
    data_dragons[color_dragon] = {name: name_dragon[name] for name in sorted_names}

for dragon_type, dragon_data in data_dragons.items():
    total_damage = 0
    total_health = 0
    total_armor = 0
    for dragon_name, stats in dragon_data.items():
        total_damage += stats[0]
        total_health += stats[1]
        total_armor += stats[2]
    avg_damage = total_damage / len(dragon_data)
    avg_health = total_health / len(dragon_data)
    avg_armor = total_armor / len(dragon_data)
    print(f"{dragon_type}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
    for dragon_name, stats in dragon_data.items():
        damage = stats[0]
        health = stats[1]
        armor = stats[2]
        print(f"-{dragon_name} -> damage: {damage}, health: {health}, armor: {armor}")

# for color, name, stats in data_dragons.items():


# print(len(data_dragons))
