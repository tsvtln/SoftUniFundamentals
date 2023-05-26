from math import floor as fl
group_size, adventuring_days = int(input()), int(input())
current_day, coins = 0, 0
for days in range(adventuring_days):
    current_day += 1
    coins += 50
    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 15 == 0:
        group_size += 5
    coins -= 2 * group_size  # for food
    if current_day % 3 == 0:
        coins -= 3 * group_size  # motivational party; drinking water
    if current_day % 5 == 0:
        coins += 20 * group_size  # boss battle
        if current_day % 3 == 0:
            coins -= 2 * group_size
split = fl(coins / group_size)
print(f'{group_size} companions received {split} coins each.')
