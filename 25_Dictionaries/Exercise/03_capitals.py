countries, capitals = input().split(', '), input().split(', ')
output = {countries[index]: capitals[index] for index in range(len(capitals))}
printing = {print(f"{country} -> {capital}") for country, capital in output.items()}
