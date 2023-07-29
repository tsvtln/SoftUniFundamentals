import re
string = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

matches = re.finditer(pattern, string)
for match in matches:
    print(match.group(), end=' ')
