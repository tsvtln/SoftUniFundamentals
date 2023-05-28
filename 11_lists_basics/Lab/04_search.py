number_of_words = int(input())
list_words = []
filter_word = input()
for words in range(number_of_words):
    word = input()
    list_words.append(word)
print(list_words)
for removing in range(len(list_words) - 1, -1, -1):
    removed = list_words[removing]
    if filter_word not in removed:
        list_words.remove(removed)
print(list_words)
