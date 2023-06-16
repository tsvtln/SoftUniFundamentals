def memory_game(sequence: list):
    command = ''
    moves = 0
    while command != 'end':
        command = input()
        if command == 'end':
            continue
        else:
            command = [int(x) for x in command.split()]
            moves += 1
            if command[0] == command[1] or any(val < 0 or val > len(sequence) - 1 for val in command):
                middle_of_sequence = len(sequence) // 2
                sequence.insert(middle_of_sequence, '-' + str(moves) + 'a')
                sequence.insert(middle_of_sequence, '-' + str(moves) + 'a')
                print('Invalid input! Adding additional elements to the board')
            elif sequence[command[0]] == sequence[command[1]]:
                print(f'Congrats! You have found matching elements - {sequence[command[0]]}!')
                if command[0] > command[1]:
                    sequence.pop(command[0])
                    sequence.pop(command[1])
                else:
                    sequence.pop(command[1])
                    sequence.pop(command[0])
            elif sequence[command[0]] != sequence[command[1]]:
                print('Try again!')
            if len(sequence) == 0:
                print(f"You have won in {moves} turns!")
                command = 'end'
    if command == 'end' and len(sequence) > 0:
        print(f"Sorry you lose :(\n{' '.join(sequence)}")
    return


entry_sequence = input().split()
memory_game(entry_sequence)
