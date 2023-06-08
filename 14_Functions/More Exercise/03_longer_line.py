from math import floor


def closer_line(arg1, arg2, arg3, arg4):
    one = arg1 + arg2
    two = arg3 + arg4
    if one > two:
        if abs(x1_1) + abs(x2_1) > abs(y1_1) + abs(y2_1):
            return f"({y1_1}, {y2_1})({x1_1}, {x2_1})"
        else:
            return f"({x1_1}, {x2_1})({y1_1}, {y2_1})"
    elif one < two:
        if abs(x1_2) + abs(x2_2) > abs(y1_2) + abs(y2_2):
            return f"({y1_2}, {y2_2})({x1_2}, {x2_2})"
        else:
            return f"({x1_2}, {x2_2})({y1_2}, {y2_2})"
    else:
        if abs(x1_2) + abs(x2_2) > abs(y1_2) + abs(y2_2):
            return f"({y1_2}, {y2_2})({x1_2}, {x2_2})"
        else:
            return f"({x1_2}, {x2_2})({y1_2}, {y2_2})"


x1_1, x2_1, y1_1, y2_1 = floor(float(input())), floor(float(input())), floor(float(input())), floor(float(input()))
x1_2, x2_2, y1_2, y2_2 = floor(float(input())), floor(float(input())), floor(float(input())), floor(float(input()))

sum_x_one = floor(abs(x1_1) + abs(x2_1))
sum_y_one = floor(abs(y1_1) + abs(y2_1))
sum_x_two = floor(abs(x1_2) + abs(x2_2))
sum_y_two = floor(abs(y1_2) + abs(y2_2))

print(closer_line(sum_x_one, sum_y_one, sum_x_two, sum_y_two))


