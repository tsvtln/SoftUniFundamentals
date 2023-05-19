snowballs_made = int(input())
highest_quality, highest_quality_weight, highest_quality_time, highest_quality_value = 0, 0, 0, 0

for snowballs in range(snowballs_made):
    weight_of_snowball = int(input())
    time_needed = int(input())
    quality = int(input())
    calculate = (weight_of_snowball / time_needed) ** quality

    if calculate > highest_quality:
        highest_quality = calculate
        highest_quality_time = time_needed
        highest_quality_weight = weight_of_snowball
        highest_quality_value = quality

print(f'{highest_quality_weight} : {highest_quality_time} = {highest_quality:.0f} ({highest_quality_value})')
