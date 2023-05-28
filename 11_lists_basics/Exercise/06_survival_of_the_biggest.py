list_of_numbers = [int(x) for x in input().split(' ')]
count_to_remove = int(input())
for removing in range(count_to_remove):
    list_of_numbers.remove(min(list_of_numbers))
# print(((str(list_of_numbers).replace('[', '')).replace(',', '')).replace(']', ''))

print(', '.join(str(item) for item in list_of_numbers))
