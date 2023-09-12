word_definitions = input().split(' | ')
teacher_test_words = input().split(' | ')
command = input()

words_dict = dict()

for word_description in word_definitions:
    word_def = word_description.split(": ")
    if word_def[0] not in words_dict.keys():
        words_dict[word_def[0]] = [word_def[1]]
    elif word_def[0] in words_dict.keys():
        words_dict[word_def[0]].append(word_def[1])

if command == 'Test':
    for word in teacher_test_words:
        if word in words_dict.keys():
            print(f"{word}:")
            for definition in words_dict[word]:
                print(f" -{definition}")

elif command == 'Hand Over':
    for words in words_dict.keys():
        print(words, end=' ')