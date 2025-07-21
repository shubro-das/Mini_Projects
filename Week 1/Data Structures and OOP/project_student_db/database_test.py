from models.student import Student
from core.database import StudentDatabase

db = StudentDatabase()

# Add student
s1 = Student("S101", "Shubro Das", 21, "A")
if db.add_student(s1):
    print("Student added!")
else:
    print("Student ID already exists!")

# Retrieve student
student = db.get_student("S102")
if student:
    print(student.display_info())
else:
    print("Student not found.")
