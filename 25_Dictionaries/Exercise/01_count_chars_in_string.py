letters, count_chars = [char for char in input()], dict()
for letter in letters:
    if letter not in count_chars and letter != ' ':
        count_chars[letter] = 1
    elif letter in count_chars and letter != ' ':
        count_chars[letter] += 1

for letter, count in count_chars.items():
    print(f"{letter} -> {count}")


