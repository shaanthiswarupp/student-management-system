from main import add_student, delete_student, get_all_students

# Create a temporary student for testing
add_student("TestDelete", 20, "Testing")

# Delete the temporary student
deleted = delete_student("TestDelete")

print("Deleted student:")
print(deleted)

# Display remaining students
print("Remaining students:")

for student in get_all_students():
    print(student)

# Try deleting a student who does not exist
unknown = delete_student("Suresh")

print("Unknown student deletion:")
print(unknown)