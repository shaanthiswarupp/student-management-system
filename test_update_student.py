from main import update_student

# Update an existing student
student = update_student("Kiran", 25, "Advanced Python")

print("Updated student:")
print(student)

# Try updating a student who does not exist
unknown = update_student("Suresh", 30, "Java")

print("Unknown student update:")
print(unknown)