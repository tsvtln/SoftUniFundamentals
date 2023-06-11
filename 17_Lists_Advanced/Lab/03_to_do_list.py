CONTINUE = True
to_do_list = []
command_list = []
while CONTINUE:
    command = input()
    if command == 'End':
        CONTINUE = False
        continue
    command_list.append(command)

command_list = sorted(command_list, key=lambda x: int(x.split('-')[0]))
for item in command_list:
    item_thing = item.split('-')
    to_do_list.append(item_thing[1])

print(to_do_list)
