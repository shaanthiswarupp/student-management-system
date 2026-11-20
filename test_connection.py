 #step -3


from database import get_connection

connection = get_connection()

try:
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("Student records in MySQL:")

    for student in students:
        print(student)

finally:
    cursor.close()
    connection.close()










# #step -2

# from database import get_connection

# connection = get_connection()

# try:
#     cursor = connection.cursor()

#     query = """
#     INSERT INTO students (name, age, course)
#     VALUES (%s, %s, %s)
#     """

#     values = ("Arun", 23, "Java")

#     cursor.execute(query, values)

#     connection.commit()

#     print("Student inserted successfully!")

# finally:
#     cursor.close()
#     connection.close()
















#step -1
#  from database import get_connection

# try:
#     connection = get_connection()

#     print("MySQL connection successful!")

#     connection.close()

#     print("MySQL connection closed.")

# except Exception as error:
#     print("MySQL connection failed!")
#     print(error)
