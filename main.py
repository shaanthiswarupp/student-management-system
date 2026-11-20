#===================== step-2===================
from database import get_connection

# CREATE: Add a new student
def add_student(name, age, course):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO students (name, age, course)
        VALUES (%s, %s, %s)
        """
        values = (name, age, course)
        cursor.execute(query, values)

        connection.commit()
        student_id = cursor.lastrowid

        return {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course
        }

    finally:
        cursor.close()
        connection.close()


#=================  step-3  =  step-2 + step-3 ========================
# READ: Get all students
def get_all_students():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM students"
        cursor.execute(query)
        students = cursor.fetchall()
        return students

    finally:
        cursor.close()
        connection.close()


#=================  step-4  =  step-2 + step-3 + step-4 ========================

# READ: Get a student by name
def get_student_by_name(name):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM students WHERE name = %s"

        cursor.execute(query, (name,))
        student = cursor.fetchone()
        return student

    finally:
        cursor.close()
        connection.close()

#=================  step-5 =  step-2 + step-3 + step-4 + step-5 ========================

# UPDATE: Update a student's details
def update_student(name, age, course):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        query = """
        UPDATE students
        SET age = %s, course = %s
        WHERE name = %s
        """
        values = (age, course, name)
        cursor.execute(query, values)
        connection.commit()

        if cursor.rowcount == 0:
            return None

        cursor.execute("SELECT * FROM students WHERE name = %s", (name,)        )

        student = cursor.fetchone()
        return student

    finally:
        cursor.close()
        connection.close()


#=================  step-6 =  step-2 + step-3 + step-4 + step-5 +step-6  ========================

# DELETE: Delete a student
def delete_student(name):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        # First, find the student
        cursor.execute( "SELECT * FROM students WHERE name = %s", (name,)         )
        student = cursor.fetchone()

        # If student does not exist
        if student is None:
            return None

        # Delete the student
        cursor.execute( "DELETE FROM students WHERE name = %s", (name,)         )

        connection.commit()
        return student

    finally:
        cursor.close()
        connection.close()











# step-1
# students = []
# def add_student(name, age, course):
#     student = {
#         "name": name,
#         "age": age,
#         "course": course
#     }
#     students.append(student)
#     return student
# def get_all_students():
#     return students


# def get_student_by_name(name):
#     for student in students:
#         if student['name'] == name:
#             return student
#     return None


# def update_student(name, age, course):
#     for student in students:
#         if student['name'] == name:
#             student['age'] = age
#             student['course'] = course
#             return student
#     return None


# def delete_student(name):
#     for student in students:
#         if student['name'] == name:
#             students.remove(student)
#             return student
#     return None


# if __name__ == "__main__":
#     add_student("Rahul", 21, "Python")
#     add_student("Priya", 22, "Java")
#     print(get_all_students())
