rows = int(input())
ships_list = []
for current_row in range(rows):
    ships = input().split(' ')
    ships_list.append(ships)
attack = input().split(' ')
destroyed = 0
for attack in attack:
    current_attack = attack.split('-')
    row = int(current_attack[0])
    column = int(current_attack[1])
    current_ship = ships_list[row]
    current = int(current_ship[column])
    if current > 0:
        current -= 1
        if current == 0:
            destroyed += 1
    current_ship[column] = str(current)
    ships_list[row] = current_ship
print(destroyed)
