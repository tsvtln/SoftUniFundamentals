def smallest(value_one, value_two, value_three):
    if value_one < value_two and value_one < value_three:
        return value_one
    elif value_two < value_one and value_two < value_three:
        return value_two
    else:
        return value_three


input_value_one = int(input())
input_value_two = int(input())
input_value_three = int(input())
print(smallest(input_value_one, input_value_two, input_value_three))
