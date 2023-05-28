command = input().split()
for number in range(len(command)):
    command[number] = -int(command[number])
print(command)
