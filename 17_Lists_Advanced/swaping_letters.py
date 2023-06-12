words = ['nqkva duma', 'druga duma', 'treta duma']
modified_words = []

for word in range(len(words)):
    current_word = list(words[word])
    memory_letter = current_word[0]
    VERTEX = True
    for i, letter in enumerate(current_word):
        if letter == current_word[0] and VERTEX:
            current_word[0], VERTEX = current_word[(len(current_word) // 2 - 1)], False
        if letter == current_word[(len(current_word) // 2 - 1)]:
            current_word[(len(current_word) // 2 - 1)] = memory_letter

    VERTEX = True
    modified_words.append(''.join(current_word))
print(modified_words)
