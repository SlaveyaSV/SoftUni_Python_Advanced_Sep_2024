def softuni_students(*args, **kwargs):
    students = {}
    for course_id, student in args:
        for id_course, course_name in kwargs.items():
            if course_id == id_course:
                students[student] = course_name

    invalid_course_students = [name[1] for name in args if name[1] not in students]

    result = ""
    for student, course in sorted(students.items()):
        result += f"*** A student with the username {student} has successfully finished the course {course}!\n"
    if invalid_course_students:
        result += f"!!! Invalid course students: {', '.join(sorted(invalid_course_students))}"

    return result


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
