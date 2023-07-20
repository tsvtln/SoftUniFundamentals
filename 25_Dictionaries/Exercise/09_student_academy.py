pair_of_rows = int(input())
students = dict()
for student_data in range(pair_of_rows):
    student = input()
    grade = float(input())
    if student in students.keys():
        students[student].append(grade)
    else:
        students[student] = [grade]

for student, grade in students.items():
    total_grade = 0
    for grades in grade:
        total_grade += grades
    total_grade = total_grade / len(grade)
    if total_grade >= 4.50:
        print(f"{student} -> {total_grade:.2f}")
