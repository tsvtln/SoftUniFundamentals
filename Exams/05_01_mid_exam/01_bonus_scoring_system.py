from math import ceil


def bonus_scoring_system(students, lectures, bonus):
    max_bonus = 0
    attended = 0
    for show_ups in range(students):
        student_attendances = int(input())
        total_bonus = student_attendances / lectures * (5 + bonus)
        if total_bonus > max_bonus:
            max_bonus = total_bonus
            attended = student_attendances
    return max_bonus, attended


entry_students = int(input())
entry_lectures = int(input())
entry_bonus = int(input())
mb, att = bonus_scoring_system(entry_students, entry_lectures, entry_bonus)
print(f'Max Bonus: {ceil(mb)}.\nThe student has attended {att} lectures.')
