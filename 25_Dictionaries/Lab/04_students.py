command, students = '', []
while True:
    command = input()
    if ':' not in command:
        break
    name, id_, course = command.split(':')
    students.append({'name': name, 'ID': id_, 'course': course})

for student in students:
    print(f"{student['name']} - {student['ID']}") if command[0:3] in student['course'] else 0
