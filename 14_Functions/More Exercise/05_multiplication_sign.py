def multiplication_sign(value_one: int, value_two: int, value_three: int) -> str:
    list_of_numbers = [value_one, value_two, value_three]
    count_negative = 0
    for number in list_of_numbers:
        if number < 0:
            count_negative += 1
    if value_one == 0 or value_two == 0 or value_three == 0:
        return 'zero'
    else:
        if count_negative == 0:
            return 'positive'
        elif count_negative == 1:
            return 'negative'
        elif count_negative == 2:
            return 'positive'
        elif count_negative == 3:
            return 'negative'


vio, vit, vith = int(input()), int(input()), int(input())
print(multiplication_sign(vio, vit, vith))
