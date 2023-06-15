find_words, command = input().split(', '), input().split(', ')
contained_words, temp_find, temp_command, temp_word, final_list = [], [], [], [], []

for word in range(len(command)):
    temp_command = [char for char in command[word]]
    for find in range(len(find_words)):
        temp_find = [char for char in find_words[find]]
        for letter in temp_command:
            temp_word.append(letter) if letter in temp_find else temp_word.clear()
            if temp_word == temp_find:
                contained_words.append(''.join(temp_find))
                temp_word.clear()
                break

for final in range(len(find_words)):
    final_list.append(find_words[final]) if find_words[final] in contained_words else ''

print(final_list)
