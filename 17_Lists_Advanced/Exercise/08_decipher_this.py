cypher, final_message = input().split(), []
for word in cypher:
    current_word = [char for char in word]
    non_num, itr, fl, letters, last_letter = 0, 0, [], [], ''
    count = sum(1 for word in current_word if word.isalpha())
    for char in current_word:
        itr += 1
        if char.isnumeric():
            fl.append(char)
        else:
            non_num += 1
        if non_num == 1:
            last_letter = char
            final_message.append(chr(int(''.join(fl))))
            final_message.append(current_word[len(current_word) - 1])
            final_message.append(' ') if count == 1 else 0
        if itr == len(current_word) and count > 1:
            final_message.append(last_letter)
            final_message.append(' ')
        final_message.append(char) if itr != len(current_word) and non_num > 1 else 0

print(''.join(final_message))
