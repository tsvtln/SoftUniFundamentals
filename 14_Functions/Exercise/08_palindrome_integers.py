def palindrome(integers_list):
    if integers_list == integers_list[::-1]:
        return True
    else:
        return False


list_of_numbers = input().split(', ')
for numbers in list_of_numbers:
    if palindrome(numbers):
        print(True)
    else:
        print(False)

