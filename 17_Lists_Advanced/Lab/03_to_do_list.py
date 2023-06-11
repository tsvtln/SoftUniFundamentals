CONTINUE = True
to_do_list, command_list = [], []


def sort_and_fill(list_of_commands):
    list_of_commands = sorted(list_of_commands, key=lambda x: int(x.split('-')[0]))
    for item in list_of_commands:
        item_thing = item.split('-')
        to_do_list.append(item_thing[1])
    print(to_do_list)
    return


while CONTINUE:
    command = input()
    if command == 'End':
        CONTINUE = False
        continue
    command_list.append(command)

sort_and_fill(command_list)
