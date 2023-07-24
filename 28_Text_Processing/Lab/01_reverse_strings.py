string = ''
while string != 'end':
    string = input()
    if string == 'end':
        continue
    print(f"{string} = {string[::-1]}")
