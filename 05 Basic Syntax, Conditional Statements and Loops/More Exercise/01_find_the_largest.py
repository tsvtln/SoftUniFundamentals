number = int(input())
list_of_digits = list(map(int, str(number)))
sort = sorted(list_of_digits, reverse=True)
sort = str(sort)
rs = ''
for a in sort:
    if a != ',' and a != '[' and a != ' ' and a != ']':
        rs += a

print(rs)
