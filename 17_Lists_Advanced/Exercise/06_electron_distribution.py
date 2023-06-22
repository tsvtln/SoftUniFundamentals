electrons = int(input())
list_electrons = []
shell = 0
while electrons > 0:
    shell += 1
    etf = 2 * shell ** 2
    if etf > electrons:
        list_electrons.append(electrons)
        electrons = 0
    else:
        electrons -= etf
        list_electrons.append(etf)

print(list_electrons)
