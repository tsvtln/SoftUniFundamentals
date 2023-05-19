is_prime = True
inp = int(input())

for i in range(2, inp):
    if inp % i == 0:
        is_prime = False

if is_prime:
    print('True')
else:
    print('False')
