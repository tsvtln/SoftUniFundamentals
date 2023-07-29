import re

sentence = input()
word_to_seek = input()

find_word = fr"{word_to_seek}\b"

count = re.findall(find_word, sentence, re.IGNORECASE)
print(len(count))


