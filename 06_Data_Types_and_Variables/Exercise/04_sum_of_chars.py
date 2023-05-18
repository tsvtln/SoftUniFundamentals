num_of_lines, sum_of_chars = int(input()), 0
for inputs in range(num_of_lines):
    char = input()
    sum_of_chars += ord(char)
print(f'"The sum equals: {sum_of_chars}"')
