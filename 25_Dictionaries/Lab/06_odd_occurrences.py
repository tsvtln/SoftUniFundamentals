words, items = input().split(), dict()
for word in words:
    word_lower = word.lower()
    if word_lower not in items:
        items[word_lower] = 0
    items[word_lower] += 1

print(' '.join([key for key, value in items.items() if value % 2 != 0]))
