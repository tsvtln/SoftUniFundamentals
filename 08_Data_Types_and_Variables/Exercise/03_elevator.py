num_of_people, capacity, courses = int(input()), int(input()), 0
while num_of_people > 0:
    num_of_people -= capacity
    courses += 1
print(courses)
