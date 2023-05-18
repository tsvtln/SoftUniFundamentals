END, VOLDEMORT = False, False
while not END:
    name = input()
    if name == 'Welcome!':
        END = True
        continue
    elif name == 'Voldemort':
        END, VOLDEMORT = True, True
        continue
    length = len(name)
    if length < 5:
        print(f"{name} goes to Gryffindor.")
    elif length == 5:
        print(f"{name} goes to Slytherin.")
    elif length == 6:
        print(f"{name} goes to Ravenclaw.")
    elif length > 6:
        print(f"{name} goes to Hufflepuff.")
if VOLDEMORT:
    print("You must not speak of that name!")
else:
    print('Welcome to Hogwarts.')
