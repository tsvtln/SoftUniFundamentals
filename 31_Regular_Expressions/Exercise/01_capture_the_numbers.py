import re
strings = input()
while strings:

    regex = r"\d+"
    find_numbers = re.findall(regex, strings)
    if find_numbers:
        print(f"{' '.join(find_numbers)}", end=' ')
    strings = input()
