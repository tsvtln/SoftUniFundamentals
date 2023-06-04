def min_max(list_of_numbers: list):
    minimum_number = min(list_of_numbers)
    maximum_number = max(list_of_numbers)
    sum_of_numbers = sum(list_of_numbers)
    return f'The minimum number is {minimum_number}\nThe maximum number is {maximum_number}\n' \
           f'The sum number is: {sum_of_numbers}'


sequence = [int(number) for number in input().split()]
print(min_max(sequence))
