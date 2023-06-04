def perfect_number(number):
    sum_of_numbers = 0
    for perfect in range(1, number):
        if number % perfect == 0:
            sum_of_numbers += perfect
    if sum_of_numbers == number:
        return True


number_entry = int(input())
if perfect_number(number_entry) is True:
    print('We have a perfect number!')
else:
    print("It's not so perfect.")

