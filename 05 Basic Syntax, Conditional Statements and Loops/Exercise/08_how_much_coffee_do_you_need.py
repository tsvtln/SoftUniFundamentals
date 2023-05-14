END, count = False, 0
while not END:
    command = input()
    if command == 'END' or command == 'end':
        END = True
        continue
    elif command == 'dog' or command == 'cat' or command == 'coding' or command == 'movie':
        count += 1
    elif command == 'DOG' or command == 'CAT' or command == 'CODING' or command == 'MOVIE':
        count += 2
    else:
        continue
    if count > 5:
        END = True
        continue
if count > 5:
    print('You need extra sleep')
else:
    print(f'{count}')
