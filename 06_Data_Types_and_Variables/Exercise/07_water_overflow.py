wt_capacity, nol, poured = 255, int(input()), 0
for liters in range(nol):
    pour = int(input())
    if wt_capacity < pour:
        print('Insufficient capacity!')
        continue
    else:
        wt_capacity -= pour
        poured += pour
print(poured)
