registered = dict()
command = ''
while command != 'end':
    command = input()
    if command == 'end':
        continue

    course, user = command.split(' : ')
    if course not in registered.keys():
        registered[course] = [user]
    else:
        registered[course].append(user)

for course, students in registered.items():
    print(f"{course}: {len(registered[course])}")
    for student in students:
        print(f"-- {student}")

