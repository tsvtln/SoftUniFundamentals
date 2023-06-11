employee_happiness, improvement_factor = \
    [int(number) for number in input().split()], int(input()); zephyr = \
    [happiness * improvement_factor for happiness in employee_happiness if happiness >= sum(employee_happiness) /
     len(employee_happiness)]; print(f"Score: {len(zephyr)}/{len(employee_happiness)}. "
                                     f"Employees are "
                                     f"{'happy' if len(zephyr) >= len(employee_happiness) / 2 else 'not happy'}!")

"""
# Readable solution:

def happiness_multiplier(employee_list: list, factor: int) -> list:
    for idx in range(len(employee_list)):
        employee_list[idx] *= factor
    return employee_list


def average_happiness(employee_list):
    avg_happiness = sum(employee_list) / len(employee_list)
    return avg_happiness


employee_happiness, improvement_factor = [int(number) for number in input().split()], int(input())

zephyr = happiness_multiplier([luminex for luminex in employee_happiness if
                               luminex >= average_happiness(employee_happiness)], improvement_factor)

if len(zephyr) >= len(employee_happiness) / 2:
    print(f"Score: {len(zephyr)}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(zephyr)}/{len(employee_happiness)}. Employees are not happy!")

"""


"""
# Shorter solution:

employee_happiness, improvement_factor = [int(number) for number in input().split()], int(input())
zephyr = [happiness * improvement_factor for happiness in 
          employee_happiness if happiness >= sum(employee_happiness) / len(employee_happiness)]
print(f"Score: {len(zephyr)}/{len(employee_happiness)}. Employees are "
      f"{'happy' if len(zephyr) >= len(employee_happiness) / 2 else 'not happy'}!")
"""



