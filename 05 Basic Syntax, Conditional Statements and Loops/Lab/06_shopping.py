b = int(input())
tp = 0
while True:
    c = input()
    if c == 'End':
        print('You bought everything needed.')
        break
    p = int(c)
    if tp + p > b:
        print('You went in overdraft!')
        break
    tp += p
