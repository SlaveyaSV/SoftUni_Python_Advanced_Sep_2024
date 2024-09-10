number_of_students = int(input())

students_data = {}

for _ in range(number_of_students):
    info = tuple(input().split())
    student, grade = info

    if student not in students_data:
        students_data[student] = []
    students_data[student].append(float(grade))

for student, grades in students_data.items():
    average = sum(grades) / len(grades)
    print(f"{student} -> {' '.join([str(f'{grade :.2f}') for grade in grades])} (avg: {average:.2f})")
