to_decipher = [ch for ch in input()]

command = ''

while command != 'Abracadabra':
    command = input()
    if command == 'Abracadabra':
        continue
    if 'Abjuration' in command:
        for idx, chr in enumerate(to_decipher):
            to_decipher[idx] = chr.upper()
        print(''.join(to_decipher))
    elif 'Necromancy' in command:
        for idx, chrr in enumerate(to_decipher):
            to_decipher[idx] = chrr.lower()
        print(''.join(to_decipher))
    elif 'Illusion' in command:
        command, index, letter = command.split()
        if int(index) > len(to_decipher) - 1 or int(index) < 0:
            print("The spell was too weak.")
        else:
            to_decipher[int(index)] = letter
            print("Done!")
    elif 'Divination' in command:
        command, first_sub, second_sub = command.split()
        joined_string = ''.join(to_decipher)
        if first_sub not in joined_string:
            continue
        else:
            new_string = joined_string.replace(first_sub, second_sub)
            to_decipher = [chr_ for chr_ in new_string]
            print(''.join(to_decipher))
    elif 'Alteration' in command:
        command, sub_string = command.split()
        joined_string = ''.join(to_decipher)
        if sub_string not in joined_string:
            print("The spell did not work!")
        else:
            new_string = joined_string.replace(sub_string, '')
            to_decipher = [char for char in new_string]
            print(''.join(to_decipher))
    else:
        print("The spell did not work!")
