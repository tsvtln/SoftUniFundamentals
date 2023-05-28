events = input().split('|')
energy = 100
coins = 100
OPEN = True
for event in events:
    event, value = event.split('-')
    value = int(value)
    if event == "rest":
        current_energy = energy
        energy += value
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event == 'order':
        if energy - 30 >= 0:
            coins += value
            energy -= 30
            print(f'You earned {value} coins.')
        else:
            energy += 50
            print(f'You had to rest!')
            continue

    else:
        if value <= coins:
            coins -= value
            print(f'You bought {event}.')
        else:
            print(f'Closed! Cannot afford {event}.')
            OPEN = False
    if not OPEN:
        break
if OPEN:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')

