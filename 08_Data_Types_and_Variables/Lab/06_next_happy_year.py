year, happy_new_year = int(input()), False
while not happy_new_year:
    year += 1
    if str(len(set((str(year))))) == str(len(str(year))):
        happy_new_year = True
        print(year)
