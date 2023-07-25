string = input()
final_text = ''
explosion_power = 0
for char in string:
    if char.isnumeric():
        explosion_power += int(char)
    if explosion_power != 0 and char != '>':
        explosion_power -= 1
        continue
    else:
        final_text += char
print(final_text)
