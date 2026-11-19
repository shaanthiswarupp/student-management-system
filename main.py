students = []
def add_student(name, age, course):
    student = {
        "name": name,
        "age": age,
        "course": course
    }
    students.append(student)
    return student
def get_all_students():
    return students


def get_student_by_name(name):
    for student in students:
        if student['name'] == name:
            return student
    return None


def update_student(name, age, course):
    for student in students:
        if student['name'] == name:
            student['age'] = age
            student['course'] = course
            return student
    return None


def delete_student(name):
    for student in students:
        if student['name'] == name:
            students.remove(student)
            return student
    return None


if __name__ == "__main__":
    add_student("Rahul", 21, "Python")
    add_student("Priya", 22, "Java")
    print(get_all_students())
