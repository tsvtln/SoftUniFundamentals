string = input()
digits = ''
alpha = ''
symbols = ''
for ch in string:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        alpha += ch
    else:
        symbols += ch
print(f"{digits}\n{alpha}\n{symbols}")
