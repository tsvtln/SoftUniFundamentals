END = False
while not END:
    string = input()
    if string == 'End':
        END = True
        continue
    elif string == 'SoftUni':
        continue
    else:
        print(''.join([char * 2 for char in string]))
