text = input()
letters = [char for char in text]
count_chars = dict()
for letter in letters:
    if letter not in count_chars and letter != ' ':
        count_chars[letter] = 1
    elif letter in count_chars and letter != ' ':
        count_chars[letter] += 1

for letter, count in count_chars.items():
    ltr = letter
    cnt = count
    print(f"{ltr} -> {cnt}")


