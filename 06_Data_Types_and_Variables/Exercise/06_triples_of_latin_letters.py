number, fl, sl, tl = int(input()), 97, 97, 97
for first_letter in range(number):
    for second_letter in range(number):
        for third_letter in range(number):
            print(f'{chr(fl + first_letter)}{chr(sl + second_letter)}{chr(tl + third_letter)}')
