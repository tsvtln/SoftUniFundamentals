command = [char for char in input()]
found_words, temp_list, big_char = [], [], True

for char in command:
    if char.isupper():
        if big_char:
            temp_list.append(char)
            big_char = False
        elif not big_char and char.isupper():
            found_words.append(''.join(temp_list))
            temp_list.clear()
            temp_list.append(char)
    else:
        temp_list.append(char)
found_words.append(''.join(temp_list))
print(', '.join(found_words))

