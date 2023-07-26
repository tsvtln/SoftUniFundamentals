entry = input().split()
result = 0
number = ''

for string in entry:
    number = ''
    for char in string:
        if char.isnumeric():
            number += char
    number = int(number)
    if string[0].isupper():
        number /= ord(string[0]) - 64
    elif not string[0].isupper():
        number *= ord(string[0]) - 96
    if string[-1].isupper():
        number -= ord(string[-1]) - 64
    elif not string[-1].isupper():
        number += ord(string[-1]) - 96
    result += number

print(f"{result:.2f}")
