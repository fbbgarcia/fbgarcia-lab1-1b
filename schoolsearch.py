def load_students(filename):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) != 6:
                print('Incorrect number of columns.')
                exit(1)
            try:
                student = {
                    'last_name': parts[0],
                    'first_name': parts[1],
                    'grade': parts[2],
                    'classroom': parts[3],
                    'bus': parts[4],
                    'gpa': parts[5]
                }
            except ValueError:
                print(f'Error processing line: {line}')
                exit(1)
            students.append(student)
    return students

def load_teachers(filename):
    teachers = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) != 3:
                print('Incorrect number of columns.')
                exit(1)
            try:
                teacher = {
                    'teacher_last_name': parts[0],
                    'teacher_first_name': parts[1],
                    'classroom': parts[2]
                }
            except ValueError:
                print(f'Error processing line: {line}')
                exit(1)
            teachers.append(teacher)
    return teachers


try:
    students = load_students('list.txt')
except FileNotFoundError:
    print('list.txt is not available.')
    exit(1)


try:
    teachers = load_teachers('teachers.txt')
except FileNotFoundError:
    print('teachers.txt is not available.')
    exit(1)


def find_students_by_lastname(students, last_name):
    found_students = [s for s in students if s['last_name'].lower() == last_name.lower()]
    for student in found_students:
        teacher = [t for t in teachers if t['classroom'] == student['classroom']]
        teacher_names = ', '.join([f"{t['teacher_last_name']},{t['teacher_first_name']}" for t in teacher])
        print(f"{student['last_name']},{student['first_name']},{student['grade']},{student['classroom']},{teacher_names}")


def find_students_by_lastname_bus(students, lastname):
    found_students = [s for s in students if s['last_name'].lower() == lastname.lower()]
    for student in found_students:
        print(f"{student['last_name']},{student['first_name']},{student['bus']}")


def find_students_by_teacher_last_name(students, teacher_last_name):
    teacher = [t for t in teachers if t['teacher_last_name'].lower() == teacher_last_name.lower()][0]
    found_students = [s for s in students if s['classroom'] == teacher['classroom']]
    for student in found_students:
        print(f"{student['last_name']},{student['first_name']}")


def find_students_by_grade(students, grade):
    found_students = [s for s in students if s['grade'] == grade]
    for student in found_students:
        print(f"{student['last_name']},{student['first_name']}")


def find_students_by_bus(students, bus):
    found_students = [s for s in students if s['bus'] == bus]
    for student in found_students:
        print(f"{student['last_name']},{student['first_name']},{student['grade']},{student['classroom']}")


def find_students_by_grade_gpa(students, grade, find_highest=True):
    students_in_grade = [s for s in students if s['grade'] == grade]
    if len(students_in_grade) == 0:
        return None

    if find_highest:
        high_student = max(students_in_grade, key=lambda s: s['gpa'])
        teacher = [t for t in teachers if t['classroom'] == high_student['classroom']]
        teacher_names = ', '.join([f"{t['teacher_last_name']},{t['teacher_first_name']}" for t in teacher])
        print(f"{high_student['last_name']},{high_student['first_name']},{high_student['gpa']},{teacher_names},{high_student['bus']}")
    else:
        low_student = min(students_in_grade, key=lambda s: s['gpa'])
        teacher = [t for t in teachers if t['classroom'] == low_student['classroom']]
        teacher_names = ', '.join([f"{t['teacher_last_name']},{t['teacher_first_name']}" for t in teacher])
        print(f"{low_student['last_name']},{low_student['first_name']},{low_student['gpa']},{teacher_names},{low_student['bus']}")


def calculate_average_gpa(students, grade):
    students_in_grade = [s for s in students if s['grade'] == grade]
    if len(students_in_grade) == 0:
        return None
    try:
        average_gpa = sum(float(s['gpa']) for s in students_in_grade) / len(students_in_grade)
        print(f"{average_gpa:.2f}")
    except ValueError:
        print("Invalid GPA.")
        exit(1)


def calculate_average(students):
    try:
        average_gpa = sum(float(s['gpa']) for s in students) / len(students)
        return average_gpa
    except ValueError:
        print('Invalid GPA.')
        exit(1)

def calculate_average_grade(students, grade):
    students_in_grade = [s for s in students if s['grade'] == grade]
    if len(students_in_grade) == 0:
        return None
    try:
        average_gpa = sum(float(s['gpa']) for s in students_in_grade) / len(students_in_grade)
        return average_gpa, len(students_in_grade)
    except ValueError:
        print('Invalid GPA.')
        exit(1)

def calculate_average_teacher(students, teacher):
    students_with_teacher = [s for s in students if s['classroom'] == teacher['classroom']]
    if len(students_with_teacher) == 0:
        return None
    try:
        average_gpa = sum(float(s['gpa']) for s in students_with_teacher) / len(students_with_teacher)
        return average_gpa, len(students_with_teacher)
    except ValueError:
        print('Invalid GPA.')
        exit(1)

def calculate_average_bus(students, bus):
    students_on_bus = [s for s in students if s['bus'] == bus]
    if len(students_on_bus) == 0:
        return None
    try:
        average_gpa = sum(float(s['gpa']) for s in students_on_bus) / len(students_on_bus)
        return average_gpa, len(students_on_bus)
    except ValueError:
        print('Invalid GPA.')
        exit(1)


def count_students_by_grade(students):
    grade_counts = {i: 0 for i in range(7)}

    try:
        for student in students:
            grade = int(student['grade'])
            if grade in [0, 1, 2, 3, 4, 5, 6]:
                grade_counts[grade] += 1
    except ValueError:
        print("Invalid grades.")
        exit(1)

    for grade in sorted(grade_counts.keys()):
        print(f"{grade}: {grade_counts[grade]}")


def count_students_by_classroom(students):
    classroom_counts = {i: 0 for i in range(12)}

    try:
        for student in students:
            classroom = int(student['classroom'])
            if classroom in [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]:
                classroom_counts[classroom-101] += 1
    except ValueError:
        print("Invalid classrooms.")
        exit(1)

    for classroom in sorted(classroom_counts.keys()):
        print(f"{classroom+101}: {classroom_counts[classroom]}")


def find_students_by_classroom(students, classroom):
    found_students = [s for s in students if s['classroom'] == classroom]
    for student in found_students:
        print(f"{student['last_name']},{student['first_name']}")


def find_teachers_by_classroom(teachers, classroom):
    found_teachers = [t for t in teachers if t['classroom'] == classroom]
    for teacher in found_teachers:
        print(f"{teacher['teacher_last_name']},{teacher['teacher_first_name']}")

def find_teachers_by_grade(teachers, grade):
    classrooms = list(set([s['classroom'] for s in students if s['grade'] == grade]))
    found_teachers = [t for t in teachers if t['classroom'] in classrooms]
    for teacher in found_teachers:
        print(f"{teacher['teacher_last_name']},{teacher['teacher_first_name']},{teacher['classroom']}")


def calculate_ss_grade(students):
    sse = 0
    means = []
    k = 0
    for grade in ['0', '1', '2', '3', '4', '5', '6']:
        students_in_grade = [s for s in students if s['grade'] == grade]
        if len(students_in_grade) == 0:
            continue
        else:
            k += 1
            mean = calculate_average_grade(students, grade)[0]
            means.append(mean)
            for s in students_in_grade:
                try:
                    sse += (float(s['gpa']) - mean)**2
                except ValueError:
                    print('Invalid GPA.')
                    exit(1)
    ssg = 0
    grand_mean = calculate_average(students)
    for mean in means:
        ssg += (mean - grand_mean)**2
    print(f'SSgrade: {ssg:.4f}, SSE: {sse:.4f}, k = {k}, n = {len(students)}')


def calculate_ss_teacher(students):
    sse = 0
    means = []
    k = 0
    for teacher in teachers:
        students_with_teacher = [s for s in students if s['classroom'] == teacher['classroom']]
        k += 1
        mean = calculate_average_teacher(students, teacher)[0]
        means.append(mean)
        for s in students_with_teacher:
            try:
                sse += (float(s['gpa']) - mean)**2
            except ValueError:
                print('Invalid GPA.')
                exit(1)
    sst = 0
    grand_mean = calculate_average(students)
    for mean in means:
        sst += (mean - grand_mean)**2
    print(f'SSteacher: {sst:.4f}, SSE: {sse:.4f}, k = {k}, n = {len(students)}')


def calculate_ss_bus(students):
    sse = 0
    means = []
    k = 0
    for bus in ['51', '52', '53', '54', '55', '56']:
        students_on_bus = [s for s in students if s['bus'] == bus]
        if len(students_on_bus) == 0:
            continue
        else:
            k += 1
            mean = calculate_average_bus(students, bus)[0]
            means.append(mean)
            for s in students_on_bus:
                try:
                    sse += (float(s['gpa']) - mean)**2
                except ValueError:
                    print('Invalid GPA.')
                    exit(1)
    ssb = 0
    grand_mean = calculate_average(students)
    for mean in means:
        ssb += (mean - grand_mean)**2
    print(f'SSbus: {ssb:.4f}, SSE: {sse:.4f}, k = {k}, n = {len(students)}')


while True:
    user_input = input("Enter command: ")

    if user_input.startswith('S:') or user_input.startswith('Student:'):

        if user_input.endswith(' B') or user_input.endswith(' Bus'):
            if user_input.startswith('S:'):
                lastname = user_input[2:].replace(' Bus', '').replace(' B', '').strip()
            else:
                lastname = user_input[8:].replace(' Bus', '').replace(' B', '').strip()
            find_students_by_lastname_bus(students, lastname)

        else:
            if user_input.startswith('S:'):
                lastname = user_input[2:].strip()
            else:
                lastname = user_input[8:].strip()
            find_students_by_lastname(students, lastname)

    elif user_input.startswith('T:') or user_input.startswith('Teacher:'):
        if user_input.startswith('T:'):
            teacher_last_name = user_input[2:].strip()
        else:
            teacher_last_name = user_input[8:].strip()
        find_students_by_teacher_last_name(students, teacher_last_name)

    elif user_input.startswith('G:') or user_input.startswith('Grade:'):
        if user_input.endswith("H") or user_input.endswith("High"):
            if user_input.startswith('G:'):
                grade = user_input.replace(' High', '').replace(' H', '')[2:].strip()
            else:
                grade = user_input.replace(' High', '').replace(' H', '')[6:].strip()
            find_students_by_grade_gpa(students, grade, True)

        elif user_input.endswith("L") or user_input.endswith("Low"):
            if user_input.startswith('G:'):
                grade = user_input.replace(' Low', '').replace(' L', '')[2:].strip()
            else:
                grade = user_input.replace(' Low', '').replace(' L', '')[6:].strip()
            find_students_by_grade_gpa(students, grade, False)

        elif user_input.endswith("T") or user_input.endswith("Teachers"):
            if user_input.startswith('G:'):
                classroom = user_input.replace(' Teachers', '').replace(' T', '')[2:].strip()
            else:
                classroom = user_input.replace(' Teachers', '').replace(' T', '')[6:].strip()
            find_teachers_by_grade(teachers, classroom)

        else:
            if user_input.startswith('G:'):
                grade = user_input[2:].strip()
            else:
                grade = user_input[6:].strip()
            find_students_by_grade(students, grade)

    elif user_input.startswith('B:') or user_input.startswith('Bus:'):
        if user_input.startswith('B:'):
            bus = user_input[2:].strip()
        else:
            bus = user_input[4:].strip()

        find_students_by_bus(students, bus)

    elif user_input.startswith('A:') or user_input.startswith('Average:'):
        if user_input.startswith('A:'):
            grade = user_input[2:].strip()
        else:
            grade = user_input[8:].strip()
        calculate_average_gpa(students, grade)

    elif user_input.startswith('I') or user_input.startswith('Info'):
        if user_input.endswith("C") or user_input.endswith("Classrooms"):
            count_students_by_classroom(students)
        else:
            count_students_by_grade(students)

    elif user_input in ['Q', 'Quit']:
        print("Quitting the program.")
        break

    elif user_input.startswith('C:') or user_input.startswith('Classroom:'):
        if user_input.endswith('S') or user_input.endswith('Students'):
            if user_input.startswith('C:'):
                classroom = user_input.replace(' Students', '').replace(' S', '')[2:].strip()
            else:
                classroom = user_input.replace(' Students', '').replace(' S', '')[10:].strip()
            find_students_by_classroom(students, classroom)

        elif user_input.endswith("T") or user_input.endswith("Teachers"):
            if user_input.startswith('C:'):
                classroom = user_input.replace(' Teachers', '').replace(' T', '')[2:].strip()
            else:
                classroom = user_input.replace(' Teachers', '').replace(' T', '')[10:].strip()
            find_teachers_by_classroom(teachers, classroom)

    elif user_input.startswith('SS') or user_input.startswith('Sum of Squares'):
        if user_input.endswith('G') or user_input.endswith('Grade'):
            if user_input.startswith('SS:'):
                classroom = user_input.replace(' Grade', '').replace(' G', '')[2:].strip()
            else:
                classroom = user_input.replace(' Grade', '').replace(' G', '')[14:].strip()
            calculate_ss_grade(students)

        elif user_input.endswith('T') or user_input.endswith('Teacher'):
            if user_input.startswith('SS:'):
                classroom = user_input.replace(' Teacher', '').replace(' T', '')[2:].strip()
            else:
                classroom = user_input.replace(' Teacher', '').replace(' T', '')[14:].strip()
            calculate_ss_teacher(students)

        elif user_input.endswith('B') or user_input.endswith('Bus'):
            if user_input.startswith('SS:'):
                classroom = user_input.replace(' Bus', '').replace(' B', '')[2:].strip()
            else:
                classroom = user_input.replace(' Bus', '').replace(' B', '')[14:].strip()
            calculate_ss_bus(students)

        else:
            calculate_average(students)


    else:
        print("Unrecognized command. Please try again.")



