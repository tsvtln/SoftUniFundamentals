key = int(input())
num_of_lines = int(input())
word = ''
for letters in range(num_of_lines):
    symbol = input()
    symbol_to_num = ord(symbol)
    symbol_to_num += key
    character = chr(symbol_to_num)
    word += character
print(word)
