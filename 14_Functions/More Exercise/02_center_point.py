from math import floor as f


def center_point(x_one, y_one, x_two, y_two):
    result1, result2 = x_one ** 2 + y_one ** 2, x_two ** 2 + y_two ** 2
    if result1 <= result2:
        closest_x, closest_y = f(x_one), f(y_one)
    else:
        closest_x, closest_y = f(x_two), f(y_two)
    return f'({closest_x}, {closest_y})'


x_one_ent, y_one_ent, x_two_ent, y_two_ent = float(input()), float(input()), float(input()), float(input())
print(center_point(x_one_ent, y_one_ent, x_two_ent, y_two_ent))
