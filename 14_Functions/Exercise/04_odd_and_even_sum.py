odd_digits, even_digits = sum(int(digit) for digit in input() if int(digit) % 2 != 0), \
    sum(int(digit) for digit in input() if int(digit) % 2 == 0)
print(f"Odd sum = {odd_digits}, Even sum = {even_digits}")



# def is_even(number):
#     if int(number) % 2 == 0:
#         return True
#     else:
#         return False
#
#
# def count_odd_even(list_of_numbers):
#     odd_numbers = 0
#     even_numbers = 0
#     for char in list_of_numbers:
#         if is_even(char):
#             even_numbers += int(char)
#         else:
#             odd_numbers += int(char)
#     return f'Odd sum = {odd_numbers}, Even sum = {even_numbers}'
#
#
# number_input = input()
# print(count_odd_even(number_input))
#
#
#
#
#
#
