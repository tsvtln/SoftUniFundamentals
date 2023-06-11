CONTINUE = True
wagons = [0 for wagon in range((int(input())))]
while CONTINUE:
    command = input().split(' ')
    if command[0] == 'End':
        CONTINUE = False
        continue
    if command[0] == 'add':
        wagons[-1] += int(command[1])
    elif command[0] == 'insert':
        wagons[int(command[1])] += int(command[2])
    elif command[0] == 'leave':
        wagons[int(command[1])] -= int(command[2])
print(wagons)

