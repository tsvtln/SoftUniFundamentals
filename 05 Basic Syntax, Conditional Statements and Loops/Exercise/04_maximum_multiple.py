divisor, boundary = int(input()), int(input())
max_number = 0

for number in range(divisor, boundary + 1):
    if number % divisor == 0 and boundary >= number > 0:
        max_number = number

print(max_number)
