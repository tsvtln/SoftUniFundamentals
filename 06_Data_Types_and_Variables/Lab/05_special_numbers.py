read = int(input())
for special in range(1, read + 1):
    if len(str(special)) == 1:
        if special == 5 or special == 7 or special == 11:
            print(f'{special} -> True')
        else:
            print(f'{special} -> False')
    elif len(str(special)) > 1:
        first_number = (special // 10) % 10
        second_number = special % 10
        if second_number + first_number == 5 or second_number + first_number == 7 or second_number + first_number == 11:
            print(f'{special} -> True')
        else:
            print(f'{special} -> False')
