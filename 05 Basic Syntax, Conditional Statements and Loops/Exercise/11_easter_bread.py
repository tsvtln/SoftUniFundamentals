# lf = loaf; prc = price
BUDGET, lf_eggs, lf_flour, lf_milk, budget, prc_flour = True, 1, 1, 0.250, float(input()), float(input())
breads, clrd_eggs = 0, 0
prc_flour *= lf_flour
prc_eggs = prc_flour * 0.75
prc_milk = prc_flour * 1.25

while BUDGET:
    money_needed = prc_flour + prc_eggs + (prc_milk * lf_milk)
    if money_needed > budget:
        BUDGET = False
        continue
    budget -= money_needed
    breads += 1
    clrd_eggs += 3
    if breads % 3 == 0:
        clrd_eggs -= breads - 2
print(f"You made {breads} loaves of Easter bread! Now you have {clrd_eggs} eggs and {budget:.2f}BGN left.")
