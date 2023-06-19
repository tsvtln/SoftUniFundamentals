def tax_calculator(details: list):
    total = 0
    for calculations in details:
        info = calculations.split()
        if info[0] == 'family':
            tax = 50 - (int(info[1]) * 5) + (int(info[2]) // 3000 * 12)
            total += tax
            print(f'A {info[0]} car will pay {tax:.2f} euros in taxes.')
        elif info[0] == 'heavyDuty':
            tax = 80 - (int(info[1]) * 8) + (int(info[2]) // 9000 * 14)
            total += tax
            print(f'A {info[0]} car will pay {tax:.2f} euros in taxes.')
        elif info[0] == 'sports':
            tax = 100 - (int(info[1]) * 9) + (int(info[2]) // 2000 * 18)
            total += tax
            print(f'A {info[0]} car will pay {tax:.2f} euros in taxes.')
        else:
            print('Invalid car type.')
    print(f'The National Revenue Agency will collect {total:.2f} euros in taxes.')


entry_details = input().split(">>")
tax_calculator(entry_details)
