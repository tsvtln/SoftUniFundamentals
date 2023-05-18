from re import findall
animals = input()
res = len(findall(r'\w+', animals))
anmtl = list(reversed(animals.split(', ')))

if anmtl[0] == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    for i in range(res):
        anml = anmtl[i]
        if anml == 'wolf':
            print(f'Oi! Sheep number {i}! You are about to be eaten by a wolf!')
