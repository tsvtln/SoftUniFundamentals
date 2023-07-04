command = ''
inventory = dict()
while command != 'statistics':
    command = input()
    if command == 'statistics':
        continue
    command = command.split(': ')
    for product in range(0, len(command), 2):
        if command[product] not in inventory:
            inventory[command[product]] = int(command[product + 1])
        else:
            inventory[command[product]] += int(command[product + 1])

print(f"Products in stock:")
for (product, quantity) in inventory.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(inventory.keys())}")
print(f"Total Quantity: {sum(inventory.values())}")
