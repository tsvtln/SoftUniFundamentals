data_elfs, command = {}, ''

while command != 'Once upon a time':
    command = input()
    if command == 'Once upon a time':
        continue

    command = command.split(' <:> ')
    dwarf_name, dwarf_hat_color, dwarf_physics = command[0], command[1], int(command[2])

    dwarf_key = (dwarf_name, dwarf_hat_color)

    if dwarf_key not in data_elfs or dwarf_physics > data_elfs[dwarf_key]:
        data_elfs[dwarf_key] = dwarf_physics

sorted_dwarfs = sorted(data_elfs.items(), key=lambda x: (-x[1], -sum(hat_key[1] == x[0][1] for hat_key in data_elfs.keys())))

for (dwarf_name, dwarf_hat_color), dwarf_physics in sorted_dwarfs:
    print(f"({dwarf_hat_color}) {dwarf_name} <-> {dwarf_physics}")

# data_elfs, command, sorted_dwarfs = dict(), '', []
# while command != 'Once upon a time':
#     command = input()
#     if command == 'Once upon a time':
#         continue
#
#     command = command.split(' <:> ')
#     dwarf_name, dwarf_hat_color, dwarf_physics = command[0], command[1], int(command[2])
#     if dwarf_name not in data_elfs:
#         data_elfs[dwarf_hat_color] = {dwarf_name: dwarf_physics}
#     if dwarf_name in data_elfs:
#         if dwarf_hat_color != data_elfs[dwarf_hat_color][dwarf_name]:
#             data_elfs[dwarf_hat_color][dwarf_name] = dwarf_physics
#         elif dwarf_hat_color == data_elfs[dwarf_hat_color][dwarf_name]:
#             if data_elfs[dwarf_hat_color][dwarf_name] < dwarf_physics:
#                 data_elfs[dwarf_hat_color][dwarf_name] = dwarf_physics
#
#
# for name, hats in data_elfs.items():
#     max_physics = max(hats.values())
#     total_count = len(hats)
#     sorted_dwarfs.append((name, max_physics, total_count))
#
# sorted_dwarfs.sort(key=lambda x: (-x[1], -x[2]))
#
# for dwarf_name, dwarf_physics, total_count in sorted_dwarfs:
#     print(f"({dwarf_name}) {list(data_elfs[dwarf_name].keys())[0]} <-> {dwarf_physics}")