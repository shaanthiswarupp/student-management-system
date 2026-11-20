
# --- step-2

from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel , Field

# from main import add_student,get_all_students,get_student_by_name,update_student,delete_student
from main import add_student,get_all_students,get_student_by_name,update_student,delete_student,get_students_by_course

# Create FastAPI application
app = FastAPI()



#---------------------------------------------------------------------------------------
# Student request format
class Student(BaseModel):
    name: str = Field(min_length=2, max_length=100 )
    age: int = Field(gt=0, le=120)
    course: str = Field(min_length=2, max_length=100)




#---------------------------------------------------------------------------------------
# Home API
@app.get("/")
def home():
    return { "message": "Student Management System API is running! " "build by sss" }






#---------------------------------------------------------------------------------------




# ========================== CREATE: Add a new student

@app.post("/students", status_code=201)
def create_student(student: Student):

    result = add_student(student.name,student.age,student.course)

    return {
        "message": "Student added successfully!",
        "student": result
    }




#==================================== READ: Get all students
@app.get("/students")
def read_students():
    students = get_all_students()
    student_list = []
    for student in students:
        student_data = {"id": student[0],"name": student[1],"age": student[2],"course": student[3] }
        student_list.append(student_data)
    return {
        "message": "Students retrieved successfully!",
        "students": student_list
    }




# ===================================READ: Get a student by name

# READ: Get a student by name
@app.get("/students/{name}")
def read_student(name: str):
    student = get_student_by_name(name)
    if student is None:
        raise HTTPException(status_code=404,detail="Student not found!")
        # return {"message": "Student not found!"}

    student_data = {"id": student[0],"name": student[1],"age": student[2],"course": student[3]}
    return {
        "message": "Student retrieved successfully!",
        "student": student_data
    }




#======================================== UPDATE: Update student details

# UPDATE: Update student details
@app.put("/students/{name}")
def update_student_api(name: str, student: Student):
    updated_student = update_student(name,student.age,student.course)
    if updated_student is None:
        raise HTTPException(status_code=404,detail="Student not found!")
    student_data = {
        "id": updated_student[0],
        "name": updated_student[1],
        "age": updated_student[2],
        "course": updated_student[3]
    }
    return {
        "message": "Student updated successfully!",
        "student": student_data
    }



# ================================== DELETE: Delete a student

# DELETE: Delete a student
@app.delete("/students/{name}")
def delete_student_api(name: str):
    deleted_student = delete_student(name)
    if deleted_student is None:
        raise HTTPException(status_code=404,detail="Student not found!")
        #return {"message": "Student not found!"}
    student_data = {"id": deleted_student[0],"name": deleted_student[1],"age": deleted_student[2],"course": deleted_student[3]}

    return {
        "message": "Student deleted successfully!",
        "student": student_data
    }



#===========================================================get_students_by_course(course) =================
# ==========================================
# READ: Get students by course

@app.get("/students/course/{course}")
def read_students_by_course(course: str):

    students = get_students_by_course(course)

    student_list = []

    for student in students:
        student_data = {
            "id": student[0],
            "name": student[1],
            "age": student[2],
            "course": student[3]
        }

        student_list.append(student_data)

    return student_list













#---------------------------------------------------------------------------------------

#step-1
# from fastapi import FastAPI

# # Create FastAPI application
# app = FastAPI()

# # First API endpoint
# @app.get("/")
# def home():
#     return {"message": "Student Management System API is running!"}
