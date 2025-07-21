# project_student_db/models/student.py

class Student:
    def __init__(self, student_id, name, age, grade):
        """
        Initializes a new student with basic attributes.
        """
        self.student_id = student_id  # Unique identifier for the student
        self.name = name              # Full name of the student
        self.age = age                # Age in years
        self.grade = grade            # Grade (e.g., "A", "B", etc.)

    def display_info(self):
        """
        Returns a string with student details.
        """
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def to_dict(self):
        """
        Converts the student object to a dictionary.
        Useful for serialization or JSON conversion.
        """
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }
    
    @staticmethod
    def from_dict(data):
        """
        Create a Student object from a dictionary.
        """
        return Student(
            data["student_id"],
            data["name"],
            data["age"],
            data["grade"]
        )