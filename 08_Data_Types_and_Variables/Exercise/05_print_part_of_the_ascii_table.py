char1, char2 = int(input()), int(input())
for ascii_char in range(char1, char2 + 1):
    ascii = chr(ascii_char)
    print(f'{ascii} ', end='')
