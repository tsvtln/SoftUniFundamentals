print([int(number) for number in input().split() if int(number) % 2 == 0])

# def is_even(number):
#     if int(number) % 2 == 0:
#         return True
#     else:
#         return False
#
#
# def deploy_even(list_of_numbers):
#     even_numbers = []
#     for number in list_of_numbers:
#         if is_even(number):
#             even_numbers.append(number)
#     return even_numbers
#
#
# receive_numbers = input().split(' ')
# print(str(deploy_even(receive_numbers)).replace("'", ''))
#
#