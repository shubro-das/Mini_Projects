# project_student_db/ui/menu.py

from core.database import StudentDatabase
from models.student import Student

def main_menu():
    db = StudentDatabase()

    while True:
        print("\n--- Student Database Menu ---")
        print("1. Add Student")
        print("2. Search Student by ID")
        print("3. List All Students")
        print("4. Update Student Info")
        print("5. Delete Student")
        print("6. Exit")


        choice = input("Enter choice (1-6): ")

        if choice == "1":
            # Add Student
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Name: ").strip()
            age = input("Enter Age: ").strip()
            grade = input("Enter Grade: ").strip()

            if not age.isdigit():
                print("Age must be a number!")
                continue

            student = Student(student_id, name, int(age), grade)
            if db.add_student(student):
                print("Student added successfully!")
            else:
                print("Student ID already exists. Try again.")

        elif choice == "2":
            # Search Student
            student_id = input("Enter Student ID to search: ").strip()
            student = db.get_student(student_id)
            if student:
                print("Student Found:")
                print(student.display_info())
            else:
                print("Student not found.")

        elif choice == "3":
            # List All Students
            students = db.get_all_students()
            if not students:
                print("No students found.")
            else:
                print("\nAll Students:")
                for s in students:
                    print(s.display_info())

        elif choice == "4":
            # Update Student Info
            student_id = input("Enter Student ID to update: ").strip()
            student = db.get_student(student_id)
            if not student:
                print("Student not found.")
                continue

            print("Leave fields blank to keep current values.")
            name = input(f"New Name (current: {student.name}): ").strip()
            age = input(f"New Age (current: {student.age}): ").strip()
            grade = input(f"New Grade (current: {student.grade}): ").strip()

            age_val = int(age) if age.isdigit() else None
            success = db.update_student(
                student_id,
                name=name if name else None,
                age=age_val,
                grade=grade if grade else None
            )
            print("Student info updated." if success else "Update failed.")

        elif choice == "5":
            # Delete Student
            student_id = input("Enter Student ID to delete: ").strip()
            confirm = input("Are you sure you want to delete this student? (y/n): ").lower()
            if confirm == "y":
                if db.delete_student(student_id):
                    print("Student deleted successfully.")
                else:
                    print("Student ID not found.")
            else:
                print("Delete cancelled.")

        elif choice == "6":
            db.save_to_file()
            print("Data saved. Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice, please enter 1-6.")
