sequence = [int(n) for n in input().split()]
word_string = ([*input()])
combinations = []
new_message = []

for combination in range(len(sequence)):
    code_extract = str(sequence[combination])
    code_combination = sum(int(digit) for digit in code_extract)
    combinations.append(code_combination)

for sen in range(len(combinations)):
    if len(word_string) < combinations[sen]:
        index_value = combinations[sen] - len(word_string)
    else:
        index_value = combinations[sen]
    new_message.append(word_string[index_value])
    word_string.pop(index_value)

print(''.join(new_message))

