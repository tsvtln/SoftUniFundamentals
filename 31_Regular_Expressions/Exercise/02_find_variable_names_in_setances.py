import re

string = input()
find_variables = r"\b_([A-Za-z0-9]+)\b"

variables = re.findall(find_variables, string)

print(f"{','.join(variables)}")

