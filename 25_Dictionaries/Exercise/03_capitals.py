countries, capitals = input().split(', '), input().split(', ')
output = {countries[index]: capitals[index] for index in range(len(capitals))}
# output = dict(zip(countries, capitals))  # zip method to create a dictionary without comprehension
printing = {print(f"{country} -> {capital}") for country, capital in output.items()}
