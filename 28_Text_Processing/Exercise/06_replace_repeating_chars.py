string = input()
last_string = ''
final_text = ''
for char in string:
    if char != last_string:
        final_text += char
        last_string = char

print(final_text)