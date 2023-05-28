factor, count, multiples_list = int(input()), int(input()), []
for items in range(factor, count * factor + 1, factor):
    multiples_list.append(items)
print(multiples_list)
