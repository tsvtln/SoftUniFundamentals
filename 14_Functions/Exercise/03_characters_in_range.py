def characters(char_one, char_two):
    list_of_characters = []
    for in_between in range(ord(char_one) + 1, ord(char_two)):
        list_of_characters.append(chr(in_between))
    return list_of_characters


input_char_one = input()
input_char_two = input()
print(' '.join(characters(input_char_one, input_char_two)))

