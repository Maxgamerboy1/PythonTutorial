students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student['name'].title())
    return students_titlecase


def print_student_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {'name': name, 'student_id': student_id}
    students.append(student)


def save_file(student):
    try:
        f = open('students.txt', 'a')
        f.write(student + '\n')
        f.close()
    except Exception:
        print('Couldn\'t save file')


def read_file():
    try:
        f = open('students.txt', 'r')
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print('Couldn\'t read file')


read_file()
print_student_titlecase()

student_name = input('Enter student name: ')
student_id = input('Enter student ID: ')

if not student_id.isdecimal():
    print('ID is not a number')
else:
    add_student(student_name, int(student_id))
    save_file(student_name)
