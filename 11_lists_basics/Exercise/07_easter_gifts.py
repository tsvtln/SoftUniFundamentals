gifts_bought = [str(bought) for bought in input().split(' ')]
HAS_MONEY = True
while HAS_MONEY:
    command = input()

    if command == 'No Money':
        HAS_MONEY = False
        continue
    else:
        command = command.split(' ')

    if command[0] == 'OutOfStock':
        if command[1] in gifts_bought:
            gifts_bought = [gift.replace(command[1], 'None') for gift in gifts_bought]

    elif command[0] == 'Required':
        index = int(command[2])
        gift = command[1]
        # try:
        #     gifts_bought[index] = gift
        # except IndexError:
        #     continue
        if 0 <= index < len(gifts_bought):
            gifts_bought[index] = gift

    elif command[0] == 'JustInCase':
        gifts_bought[-1] = command[1]

# print(f"{gifts_bought for _ in len(gifts_bought): if 'None' in }")

for element in gifts_bought:
    if element != 'None':
        print(element, end=' ')
