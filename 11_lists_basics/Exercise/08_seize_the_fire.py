list_of_fires = input().split('#')
available_water = int(input())
High = range(81, 126)
Medium = range(51, 81)
Low = range(1, 51)
effort = 0
total_fire = 0

print("Cells:")
for fires_cells in list_of_fires:
    type_of_fire, value_of_cell = fires_cells.split(' = ')
    # print(type_of_fires, value_of_cell)
    value_of_cell = int(value_of_cell)
    if type_of_fire == 'High':
        if value_of_cell in High:
            if available_water >= value_of_cell:
                available_water -= value_of_cell
                effort += value_of_cell * 0.25
                total_fire += value_of_cell
                print(f" - {value_of_cell}")
        else:
            continue
    elif type_of_fire == 'Medium':
        if value_of_cell in Medium:
            if available_water >= value_of_cell:
                available_water -= value_of_cell
                effort += value_of_cell * 0.25
                total_fire += value_of_cell
                print(f" - {value_of_cell}")
        else:
            continue
    elif type_of_fire == 'Low':
        if value_of_cell in Low:
            if available_water >= value_of_cell:
                available_water -= value_of_cell
                effort += value_of_cell * 0.25
                total_fire += value_of_cell
                print(f" - {value_of_cell}")
        else:
            continue

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
