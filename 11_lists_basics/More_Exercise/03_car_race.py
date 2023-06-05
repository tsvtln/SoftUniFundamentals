race_times = [int(time) for time in input().split()]
times_split = len(race_times) // 2
first_car_times = []
second_car_times = []
total_time_first_car = 0
total_time_second_car = 0
for car_times in range(1):
    left_car = race_times[:times_split]
    right_car = race_times[times_split + 1:]
    for car in range(times_split):
        first_car_times.append(left_car[car])
        second_car_times.append(right_car[car])

second_car_times.reverse()

for first_car in first_car_times:
    total_time_first_car += first_car
    if first_car == 0:
        total_time_first_car -= total_time_first_car * 0.2

for second_car in second_car_times:
    total_time_second_car += second_car
    if second_car == 0:
        total_time_second_car -= total_time_second_car * 0.2

if total_time_first_car < total_time_second_car:
    print(f'The winner is left with total time: {total_time_first_car:.1f}')
else:
    print(f'The winner is right with total time: {total_time_second_car:.1f}')

# print(total_time_first_car, total_time_second_car)
