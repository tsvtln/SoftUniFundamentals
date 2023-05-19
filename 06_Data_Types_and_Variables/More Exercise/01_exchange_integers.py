a, b = int(input()), int(input())
a_temp, b_temp = a, b
a, b = b_temp, a_temp
print(f'Before:\na = {a_temp}\nb = {b_temp}\nAfter:\na = {a}\nb = {b}')
