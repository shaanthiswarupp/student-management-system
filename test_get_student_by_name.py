
from main import get_student_by_name

student = get_student_by_name("Kiran")

print("Student found:")
print(student)

print("Searching for unknown student:")

unknown = get_student_by_name("Suresh")

print(unknown)
