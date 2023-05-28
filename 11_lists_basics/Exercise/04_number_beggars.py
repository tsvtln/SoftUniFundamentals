money_acquired, number_of_beggars, money_of_beggars, beggar = [int(x) for x in input().split(', ')], int(input()), [], 0
while beggar < number_of_beggars:
    current_money = 0
    for money in range(beggar, len(money_acquired), number_of_beggars):
        current_money += money_acquired[money]
    beggar += 1
    money_of_beggars.append(current_money)
print(money_of_beggars)
