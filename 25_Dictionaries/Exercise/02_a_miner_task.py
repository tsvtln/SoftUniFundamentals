command, items = '', dict()

while command != 'stop':
    command = input()
    if command == 'stop':
        continue
    value = int(input())
    if command not in items:
        items[command] = value
    else:
        items[command] += value

for k, v in items.items():
    print(f"{k} -> {v}")
