def tribonacci_sequence(value: int):
    first_number = 1
    second_number = 1
    third_number = 2
    for number in range(1, value + 1):
        result = 0
        cycle_value = (number - 1) % 3 + 1
        # print(cycle_value)
        if number <= 3:
            if number == 1:
                print(first_number, end=' ')
            elif number == 2:
                print(second_number, end=' ')
            elif number == 3:
                print(third_number, end=' ')
        else:
            result = first_number + second_number + third_number
            print(result, end=' ')
            first_number = second_number
            second_number = third_number
            third_number = result

    return


value_entry = int(input())
tribonacci_sequence(value_entry)
