# project_student_db/core/database.py

import os
import json
from models.student import Student

class StudentDatabase:
    def __init__(self, file_path='students.json'):
        """
        Initializes an empty dictionary to store student records.
        Keys: student_id (string)
        Values: Student objects
        """
        self.students = {}
        self.file_path = file_path
        self.load_from_file()

    def add_student(self, student: Student):
        """
        Adds a new student to the database.
        Returns True if successful, False if ID already exists.
        """
        if student.student_id in self.students:
            return False  # Duplicate ID
        self.students[student.student_id] = student
        return True

    def get_student(self, student_id):
        """
        Retrieves a student by their ID.
        Returns the Student object or None if not found.
        """
        return self.students.get(student_id)

    def get_all_students(self):
        """
        Returns a list of all student objects.
        """
        return list(self.students.values())
    
    def update_student(self, student_id, name=None, age=None, grade=None):
        """
        Updates the student's info if found.
        Only updates fields that are not None.
        Returns True if updated, False if not found.
        """
        student = self.students.get(student_id)
        if student:
            if name:
                student.name = name
            if age:
                student.age = age
            if grade:
                student.grade = grade
            return True
        return False

    def delete_student(self, student_id):
        """
        Deletes a student by ID.
        Returns True if deleted, False if not found.
        """
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False
    
    def save_to_file(self):
        """
        Saves the current students to a JSON file.
        """
        data = [s.to_dict() for s in self.students.values()]
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self):
        """
        Loads students from a JSON file into the database.
        This method should be implemented to read from self.file_path.
        """
        if not os.path.exists(self.file_path):
            return False
        
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                for student_data in data:
                    student = Student.from_dict(student_data)
                    self.students[student.student_id] = student
        except Exception as e:
            print(f'Error loading data from file : {e}')