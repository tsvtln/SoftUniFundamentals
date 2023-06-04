def sum_numbers(value_one: int, value_two: int) -> int:
    return value_one + value_two


def subtract(summ: int, value_three: int) -> int:
    return summ - value_three


def add_and_subtract(value_one: int, value_two: int, value_three: int) -> int:
    sum_calculation = sum_numbers(value_one, value_two)
    subtract_calculation = subtract(sum_calculation, value_three)
    return subtract_calculation


input_one = int(input())
input_two = int(input())
input_three = int(input())
print(add_and_subtract(input_one, input_two, input_three))
