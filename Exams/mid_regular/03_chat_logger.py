command, flst = '', []
while command != 'end':
    command = input()
    if command == 'end':
        continue
    else:
        command = command.split()
    if command[0] == 'Chat':
        flst.append(command[1])
    elif command[0] == 'Delete':
        if command[1] in flst:
            flst.remove(command[1])
        else:
            continue
    elif command[0] == 'Edit':
        if command[1] in flst:
            idx = flst.index(command[1])
            flst[idx] = command[2]
        else:
            continue
    elif command[0] == 'Pin':
        if command[1] in flst:
            idx = flst.index(command[1])
            flst.pop(idx)
            flst.append(command[1])
        else:
            continue
    elif command[0] == 'Spam':
        for word in command:
            if word != 'Spam':
                flst.append(word)

print('\n'.join(flst))
