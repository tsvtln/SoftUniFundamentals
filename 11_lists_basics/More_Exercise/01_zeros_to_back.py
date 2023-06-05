entry = [int(n) for n in input().split(', ')]
current_list = []
for number in entry:
    if number != 0:
        current_list.append(number)
for zero in entry:
    if zero == 0:
        current_list.append(zero)
print(current_list)
