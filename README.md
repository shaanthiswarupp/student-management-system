# Student Management System



A beginner-friendly Student Management System built using Python, MySQL, and FastAPI.



## Features



- Add a new student

- View all students

- Search for a student by name

- Update student details

- Delete a student

- Validate student input

- Handle HTTP errors



## Technologies Used



- Python

- MySQL

- FastAPI

- Uvicorn

- PyMySQL

- Pydantic

- python-dotenv



## Project Files



- `app.py` - FastAPI application and API endpoints

- `main.py` - Student CRUD operations

- `database.py` - MySQL connection

- `requirements.txt` - Python dependencies

- `.env` - Database configuration (private)

- `.gitignore` - Files excluded from Git



## Database Setup



Create the database:



```sql

CREATE DATABASE student_management_db;

```



Create the table:



```sql

USE student_management_db;



CREATE TABLE students (

   id INT AUTO_INCREMENT PRIMARY KEY,

   name VARCHAR(100) NOT NULL,

   age INT NOT NULL,

   course VARCHAR(100) NOT NULL

);

```



## Environment Variables



Create a `.env` file in the project root:



```env

DB_HOST=localhost

DB_PORT=3306

DB_USER=root

DB_PASSWORD=your_mysql_password

DB_NAME=student_management_db

```



Replace `your_mysql_password` with your actual MySQL password.



Never upload `.env` to GitHub.



## Installation



Create a virtual environment:



```powershell

python -m venv venv

```



Activate it:



```powershell

.\\venv\\Scripts\\Activate.ps1

```



Install dependencies:



```powershell

pip install -r requirements.txt

```



## Run the Application



```powershell

python -m uvicorn app:app --reload

```



API URL: http://127.0.0.1:8000



Swagger documentation: http://127.0.0.1:8000/docs



## API Endpoints



| Method | Endpoint | Purpose |

|---|---|---|

| GET | `/` | Check API |

| POST | `/students` | Add student |

| GET | `/students` | Get all students |

| GET | `/students/{name}` | Search student |

| PUT | `/students/{name}` | Update student |

| DELETE | `/students/{name}` | Delete student |



## Run Tests



```powershell

python -m pytest

```



## HTTP Status Codes



- `200` - Successful request

- `201` - Student created

- `404` - Student not found

- `422` - Invalid input



## Learning Objective



This project demonstrates how Python, MySQL, and FastAPI work together to build a REST API with database-backed CRUD operations.



